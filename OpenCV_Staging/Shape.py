import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    ret,thresh = cv2.threshold(frame,127,255,1)
    
    contours,h = cv2.findContours(thresh,1,2)
    #params.filterByColor = 1
    #params.blobColor = 200
    
    # Our operations on the frameS come here

    #result is dilated for marking the corners, not important
    
    for cnt in contours:
        approx = cv2.approxPolyDP(cnt,0.01*cv2.arcLength(cnt,True),True)
        print len(approx)
        if len(approx)==5:
            print "pentagon"
            cv2.drawContours(gray,[cnt],0,255,-1)
        elif len(approx)==3:
            print "triangle"
            cv2.drawContours(gray,[cnt],0,(0,255,0),-1)
        elif len(approx)==4:
            print "square"
            cv2.drawContours(gray,[cnt],0,(0,0,255),-1)
        elif len(approx) == 9:
            print "half-circle"
            cv2.drawContours(gray,[cnt],0,(255,255,0),-1)
        elif len(approx) > 15:
            print "circle"
            cv2.drawContours(gray,[cnt],0,(0,255,255),-1)

    # Threshold for an optimal value, it may vary depending on the image.

    # Display the resulting frame
    cv2.imshow('frame',gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
'''
import numpy as np
import cv2

img = cv2.imread('shapes.png')
gray = cv2.imread('shapes.png',0)

ret,thresh = cv2.threshold(gray,127,255,1)

contours,h = cv2.findContours(thresh,1,2)

for cnt in contours:
    approx = cv2.approxPolyDP(cnt,0.01*cv2.arcLength(cnt,True),True)
    print len(approx)
    if len(approx)==5:
        print "pentagon"
        cv2.drawContours(img,[cnt],0,255,-1)
    elif len(approx)==3:
        print "triangle"
        cv2.drawContours(img,[cnt],0,(0,255,0),-1)
    elif len(approx)==4:
        print "square"
        cv2.drawContours(img,[cnt],0,(0,0,255),-1)
    elif len(approx) == 9:
        print "half-circle"
        cv2.drawContours(img,[cnt],0,(255,255,0),-1)
    elif len(approx) > 15:
        print "circle"
        cv2.drawContours(img,[cnt],0,(0,255,255),-1)

cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
'''
