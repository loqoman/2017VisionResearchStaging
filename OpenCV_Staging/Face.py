import numpy
import cv2

#Print ("Version NumPy:" + numpy .__ version__)
#Print ("Version OpenCV:" + cv2 .__ version__)

#This is the code takes a while to recognize the camera depending on your computer

################################################## #################

import numpy as np

import cv2

#load the template and initialize the webcam:
Face_cascade = cv2.CascadeClassifier ('haarcascade_frontalface_alt.xml')
Cap = cv2.VideoCapture(0)

While (True)
    #Let's read a frame and save it.
    ret, img = cap.read()
    #converted the image to black and white
    Gray = cv2.cvtColor (img, cv2.COLOR_BGR2GRAY)

    # Look for the coordinates of the faces (if any) and
    #We keep your position
    Faces = face_cascade.detectMultiScale (gray, 1.3, 5)

    #Draw a rectangle in the coordinates of each face
    For (x, y, w, h) in faces:
        Cv2.rectangle (img, (x, y), (x + w, y + h), (125,255,0), 2)
        Cv2.rectangle (img, (x, y), (x + w, y + h), (50,55,0), 1)

    #We show the image
    Cv2.imshow ('img', img)
    
    #with the 'q' key we exit the program
    If cv2.waitKey (1) & 0xFF == ord ('q'):
        Break
Cap.release ()
Cv2.destroyAllWindows ()
################################################## ##################