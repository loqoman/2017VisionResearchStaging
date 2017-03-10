

#Print ("Version NumPy:" + numpy .__ version__)
#Print ("Version OpenCV:" + cv2 .__ version__)

#This is the code takes a while to recognize the camera depending on your computer

################################################## #################

import numpy as np

import cv2

#load the template and initialize the webcam:
face_cascade = cv2.CascadeClassifier ('C:\Users\clarkdar000\Desktop\opencv-master\data\haarcascades\haarcascade_eye.xml')
#This is what we are looking for. Look at the harrcascades to see more
cap = cv2.VideoCapture(0)

while(True):

    #Let's read a frame and save it.
    ret, img = cap.read()
    #converted the image to black and white
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Look for the coordinates of the faces (if any) and
    #We keep your position
    Faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    #Draw a rectangle in the coordinates of each face
    for (x, y, w, h) in Faces:
        cv2.rectangle (img, (x, y), (x + w, y + h), (125,255,0), 2)
        cv2.rectangle (img, (x, y), (x + w, y + h), (50,55,0), 1)

    #We show the image
    cv2.imshow ('img', img)
    
    #with the 'q' key we exit the program
    if cv2.waitKey (1) & 0xFF == ord ('q'):
        break
cap.release()
cv2.destroyAllWindows()
################################################## ##################