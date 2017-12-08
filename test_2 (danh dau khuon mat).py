# Lib to numeric analysis and computer vision (opencv)
import numpy as np
import cv2
# Lib to download stuff from Web
import urllib
# Download the URL and save it to the specified file (change the URL for your need)
#urllib.urlretrieve("http://www.gunnerkrigg.com/comics/00000001.jpg", "file.jpg")
# Load an color image in color
img = cv2.imread('dwayne_johnson.jpg')
# Load the Cascade file, grab it from https://raw.githubusercontent.com/shantnu/FaceDetect/master/haarcascade_frontalface_default.xml
cascPath = 'hasCascade.xml'
faceCascade = cv2.CascadeClassifier(cascPath)
# Convert image to gray (hmm we need to change that later to detect skin color...)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# Detect faces in the image
faces = faceCascade.detectMultiScale(
  gray,
  scaleFactor=1.1,
  minNeighbors=5,
  minSize=(30, 30),
  flags = cv2.CASCADE_SCALE_IMAGE
)
# Print how many faces were found
print ("Found {0} faces!".format(len(faces)) )

# Draw a rectangle around the faces in the original image

# Vẽ một khung xung quanh khuôn mặt
for (x, y, w, h) in faces:
  cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)
cv2.imshow("Faces found" ,img)
cv2.waitKey(0)


