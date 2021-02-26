import cv2 as cv
import sys
import numpy as np

# create a black image
img = np.zeros((512,512,3), np.uint8)

# Draw a line
cv.line(img,(0,0),(511,511),(255,0,0),5)

#Draw rectangle
cv.rectangle(img,(384,0),(510,128),(0,255,0),3)

# display image
cv.imshow("Display: ", img)

k = cv.waitKey(0)

#close with "s" key
if k == ord("s"):
    cv.imwrite("people.jpg",img)