import requests
import os
import time
import argparse

class api:
	def __init__(self, url = "http://localhost:3000/upload"):
		self.url = url
		self.dirs=[]

	def upload_images(self,folder):
		self.dir=[]
		self.dirs = os.listdir(folder)
		multiple_images = []
		for d in self.dirs:
			d = os.path.join(folder,d)
			files = ('images',(d.split('/')[1] ,open(d,"rb"), 'image/jpg'))
			multiple_images.append(files)

		try:		
			r = requests.post(url = self.url ,files =multiple_images)
			print r.text
		except requests.exceptions.RequestException as e:
			print '[Fatal error] : %s'%(e)


	def clear(self, folder):
		print "[Info]: in clear"
		for d in self.dirs:
			os.remove(str(folder)+str(d))
	def halt(self,t):
		time.sleep(t)

	def get(self):
		r = requests.get(url = "http://35.200.255.243")
		print r.text
		print r.status_code
if __name__ == '__main__':

	parser = argparse.ArgumentParser()
	parser.add_argument("--production",help="To connect to cloud, by default it runs locally",
						action="store_true")

	args = parser.parse_args()

	if(args.production):
		a= api(url = "http://35.200.255.243/upload")
	else:
		a  = api(url="http://localhost:3000/upload")

	a.upload_images("RecognizedFaces/")
