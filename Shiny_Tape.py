import numpy as np
import cv2
from matplotlib import pyplot as plt



cap = cv2.VideoCapture(0)

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    blur = cv2.medianBlur(frame,13)
    #result is dilated for marking the corners, not important

    '''
    Filtering the white
    '''
    hsv = cv2.cvtColor(blur, cv2.COLOR_BGR2HSV)

    #In testing!!!
    sensitivity = 3
    lower_white = np.array([0,0,255-sensitivity])
    upper_white = np.array([255,sensitivity,255])

    mask = cv2.inRange(hsv, lower_white, upper_white)
    # Frame is target, res is output
    res = cv2.bitwise_and(frame,frame, mask= mask)
    #Grayscale
    draw = cv2.cvtColor(res, cv2.COLOR_BGR2GRAY)    



    edges = cv2.Canny(draw,60,0)
    
    #Perhaps gray, then edges?

    # Finding contours from *edges*
    contours,h = cv2.findContours(edges,1,2)
    #print(contours)

    #In the form of (contours, eplison, True[?])
    num_squares = 0
    for cnt in contours:
	num_squares += 1 
	epsilon = 0.1*cv2.arcLength(cnt,True)   
	approx = cnt #cv2.approxPolyDP(cnt,epsilon,True) 	
	# Approximating the rectangles basically is bad with the amount of light filtering going on.

    #cv2.drawContours(draw, contours, -1, (0,255,0), 3)
        rect = cv2.minAreaRect(approx)

	tilt = int(rect[2])
        print("Rect[2] is currently at: ", tilt)
	if (rect[2] > -100) & (rect[2] < -70): #Looking for squares that are only straight  
            #Low point         High point
            #print("Passed!")
            box = cv2.cv.BoxPoints(rect)
	    box = np.int0(box)
	
	    cv2.drawContours(draw,[box],0,(0,0,255),2)
	    cv2.drawContours(frame,[box],0,(0,0,255),2)
	    print("The center of square " ,num_squares , "Is at: " , box[1])

    # Threshold for an optimal value, it may vary depending on the image.

    # Display the resulting frame
    
    cv2.imshow('blur',blur)
    cv2.imshow('Draw',draw)
    cv2.imshow('Edges',edges)
    cv2.imshow('frame', frame)
    #cv2.imshow('grey',gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
