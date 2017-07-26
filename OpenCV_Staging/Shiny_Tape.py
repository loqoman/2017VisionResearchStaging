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
    #edges = cv2.Canny(blur,60,0)
    edges = cv2.cvtColor(blur, cv2.COLOR_BGR2GRAY)
    
    draw = cv2.cvtColor(blur, cv2.COLOR_BGR2GRAY)
    # Finding contours
    contours,h = cv2.findContours(draw,1,2)
    print(contours)

    #In the form of (contours, eplison, True[?])
    for cnt in contours:

    
        rect = cv2.minAreaRect(cnt)
        box = cv2.cv.BoxPoints(rect)
        box = np.int0(box)
        cv2.drawContours(draw,[box],0,(0,0,255),2)

    # Threshold for an optimal value, it may vary depending on the image.

    # Display the resulting frame
    
    cv2.imshow('blur',blur)
    cv2.imshow('Draw',draw)
    cv2.imshow('Edges',edges)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
