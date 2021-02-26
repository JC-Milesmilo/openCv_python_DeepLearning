import cv2 as cv
import numpy as np

cap = cv.VideoCapture(0)
if not cap.isOpened():
    print("Cannot open camera")
    exit()
while True:
    #capture frame
    ret, frame = cap.read()

    #if frame doesn't works
    if not ret:
        print("Can't receive frame")
        break
    #put gray scale
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    #display
    cv.imshow("frame", gray)
    if cv.waitKey(1) == ord('q'):
        break
# when finish well
cap.realese()
cv.destroyAllwindows()