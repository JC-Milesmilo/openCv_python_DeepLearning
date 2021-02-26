import cv2 as cv
import sys

img = cv.imread("people.jpg")
# if image couldn't open
if img is None:
    sys.exit("could not read")

# display image
cv.imshow("Display: ", img)
k = cv.waitKey(0)

#close with "s" key
if k == ord("s"):
    cv.imwrite("people.jpg",img)