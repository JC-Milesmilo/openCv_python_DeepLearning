import numpy as np
import cv2 as cv

img = cv.imread('./imgs/people.jpg')

px = img[100,100]
print(px)

#access to blue pixel
blue = img[100,100,0]
print(blue)

#modify pixels value
img[100,100] = [255,255,255]
print(img[100,100])

#access RED value
img.item(10,10,2)

#modify RED value
img.itemset((10,10,2),100)
img.item(10,10,2)

#image propierties
print(img.shape)
print(img.dtype)

#obtain some region of image
face = img[280:340,330:390]
img[ 273:333, 100:100 ] = face
cv.imshow("Display: ", img)
k = cv.waitKey(0)