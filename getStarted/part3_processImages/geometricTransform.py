import cv2 as cv
import numpy as np

flags = [i for i in dir(cv) if i.startswith('COLOR_')]
#print(flags)

cap_video = cv.VideoCapture(0)

while (1):
    #take each frame
    _, frame = cap_video.read()

    #convert BGR to HSV
    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)

    # define range of blue color in HSV
    lower_blue = np.array([110,50,50])
    upper_blue = np.array([130,255,255])

    # Threshold the hsv image to get only color blue
    mask = cv.inRange(hsv,lower_blue,upper_blue)

    #Bitwise-AND mas and origin al image
    res = cv.bitwise_and(frame,frame, mask= mask)

    cv.imshow('frame', frame)
    cv.imshow('mask', mask)
    cv.imshow('res', res)

    key = cv.waitKey(5) & 0xFF
    if key == 27:
        break

cv.destroyAllWindows()