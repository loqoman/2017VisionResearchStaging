#First we need to load the required XML classifiers. Then load our input image (or video) in grayscale mode.

import numpy as np 	#Imports
import cv2			#Importing OpenCV!

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')	#Both of these files are inside the opencv library.
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')					#Becuase I am at school I cant do that quite yet
																			#These XML's seem to be part of the grayscale and regogntion formulas.
img = cv2.imread('sachin.jpg')					#Opening a image
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)	#Opening the 'gray' constant from opencv

# Now we find the faces in the image. If faces are found
# , it returns the positions of detected faces as Rect(x,y,w,h).
# Once we get these locations, we can create a ROI for the face and apply eye detection on this ROI
# (since eyes are always on the face !!! )

faces = face_cascade.detectMultiScale(gray, 1.3, 5)
for (x,y,w,h) in faces:

    img = cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2) #Drawing a rectangle using openCV's rectangle library

    roi_gray = gray[y:y+h, x:x+w]	#I *belive* that this is converting to grayscale
    roi_color = img[y:y+h, x:x+w]	#More 'Grayscale'

    eyes = eye_cascade.detectMultiScale(roi_gray)
    for (ex,ey,ew,eh) in eyes:
        cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)

cv2.imshow('img',img) 	#Showing the image
cv2.waitKey(0)			#Waiting for...Something?		
cv2.destroyAllWindows()	#Closing all the windows