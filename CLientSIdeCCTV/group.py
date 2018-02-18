import os
from API import api
app = api()
while(1):
	app.send("RecognizedFaces/")
	app.clear("RecognizedFaces/")
	app.halt(60)
	print " again"