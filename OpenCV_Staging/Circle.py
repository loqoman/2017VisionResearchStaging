import numpy as np
import cv2, time

cap = cv2.VideoCapture(0)

for i in range (10):
    ret, img = cap.read()
    if ret:
        break
else:
    # capture failed even after 10 tries
    raise MyExceptiom("Video driver does not like me.")

time.sleep(2)

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read(0)
    frame = cv2.medianBlur(frame,5)

    print(frame.shape)

    cimg = cv2.cvtColor(frame,cv2.COLOR_GRAY2BGR)

    circles = cv2.HoughCircles(frame,cv2.HOUGH_GRADIENT,1,20,
                            param1=50,param2=30,minRadius=0,maxRadius=0)

    # Our operations on the frame come here
    #changing the frame to gray
    circles = np.uint16(np.around(circles))
    for i in circles[0,:]:
        # draw the outer circle
        cv2.circle(cimg,(i[0],i[1]),i[2],(0,255,0),2)
        # draw the center of the circle
        cv2.circle(cimg,(i[0],i[1]),2,(0,0,255),3)



    #result is dilated for marking the corners, not important

    # Threshold for an optimal value, it may vary depending on the image.

    # Display the resulting frame
    cv2.imshow('frame',cimg)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
'''
import cv2
import numpy as np

img = cv2.imread('opencv_logo.png',0)
img = cv2.medianBlur(img,5)
cimg = cv2.cvtColor(img,cv2.COLOR_GRAY2BGR)

circles = cv2.HoughCircles(img,cv2.HOUGH_GRADIENT,1,20,
                            param1=50,param2=30,minRadius=0,maxRadius=0)

circles = np.uint16(np.around(circles))
for i in circles[0,:]:
    # draw the outer circle
    cv2.circle(cimg,(i[0],i[1]),i[2],(0,255,0),2)
    # draw the center of the circle
    cv2.circle(cimg,(i[0],i[1]),2,(0,0,255),3)

cv2.imshow('detected circles',cimg)
cv2.waitKey(0)
cv2.destroyAllWindows()
'''