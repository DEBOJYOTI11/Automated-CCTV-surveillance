import numpy as np
import cv2
import dlib
import datetime
import time
import logging
from skimage.measure import compare_ssim



class Frame:

	#constructor , takes path of the video default  
	def __init__(self, DatasetPath ,path=0 ,label = 1 ,threshold=0.9):
		self.path = path
		self.DatasetPath = DatasetPath
		self.cap  = cv2.VideoCapture(self.path)
		self.eye_cascade = cv2.CascadeClassifier('Resource/haarcascade_eye.xml') 
		self.face_cascade = cv2.CascadeClassifier('Resource/haarcascade_frontalface_default.xml')
		self.label = label
		self.threshold = threshold


	#destroy all windows
	def destroy(self):
		self.cap.release()
		cv2.destroyAllWindows()

	def showimage(self, img,faces):
		for (x,y,w,h) in faces:
			cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
		cv2.imshow("frame",img)

	def preprocess(self, img):
		
		#image resize
		#image highlight (histogram quilization)
		print img.shape
		return img

	#save image to disk
	def save(self, image):
		image = self.preprocess(image)
		image = cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)
		localtime = datetime.datetime.now().strftime("%I:%M%p on %B %d, %Y")
		title = self.DatasetPath+ str(self.label) + '-'+ str(localtime) + ".jpg"
		print '[Info] Saved ',title
		cv2.imwrite(title, image)

	#templat match : template = Region of interest (face)
	#big picturem  = current frame under processing
	def match(self, roi,face):
		
		face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
		roi  =  roi.astype(np.uint8)
		face =  face.astype(np.uint8)
		
		w,h = roi.shape[::-1]
		res = cv2.matchTemplate(face, 
								roi, 
								cv2.TM_CCOEFF_NORMED)

		
		locations = np.where(res>=(self.threshold))
		if locations is None:
			self.label+=1
			return False


		if(len(locations)==1):
			return False
		return True

	def run(self):
		#face or tempplate
		roi  = None
		counter=0
		f = None
		while(True):
			if not self.cap.isOpened():
					self.cap.open(self.path)

			flag, img = self.cap.read()
			if not flag:
				print '[Error] Bad frame detected'
				break

			gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
			# if(f is None):
			# 	f = gray
			# try:
			# 	compare = compare_ssim(f,gray)
			# except:
			# 	pass
			
			# if(compare<0.85):
			# 	print compare
			# 	cv2.imshow("frame",gray)
			# 	f= gray
			# if counter>1000:
			# 	break
			# continue
			#check if the current region of interest(template) matches with the current frame.
			#if mathed then ignore the current frame
			
			faces = self.face_cascade.detectMultiScale(gray, 1.4, 6)
			print len(faces)
			continue
			for (x,y,w,h) in faces:
				
				cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
				roi = gray[y:y+h, x:x+w]
				if roi is None:
					self.save(roi)
				elif self.match(roi,img):
					print '[Info] Frame detected'
					self.save(roi)

			#display image on the frame
			cv2.imshow("Video Streaming",img)
			counter+=1
			

			if cv2.waitKey(1) & 0xFF == ord('q'):
				break


	def recognizeEyes(self):
		eyes = self.eye_cascade.detectMultiScale(gray)

		for (ex,ey,ew,eh) in eyes:
			cv2.rectangle(img,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)


frame  = Frame("video.avi")
frame.run()
frame.destroy()