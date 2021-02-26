import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

#train data
trainData = np.random.randint(0,100,(25,2)).astype(np.float32)

#label each one either red or blue with 0 and 1
response = np.random.randint(0,2,(25,1)).astype(np.float32)

# take red neighbours and plot them
red = trainData[response.ravel()==0]
plt.scatter(red[:,0],red[:,1],80, 'r', '^')

#  take blue neighbours and plot them
blue = trainData[response.ravel()==1]
plt.scatter(blue[:,0],blue[:,1],80, 'b', 's')

#plt.show()

# select k
newcomer = np.random.randint(0,100,(1,2)).astype(np.float32)
plt.scatter(newcomer[:,0],newcomer[:,1],80,'g','o')
knn = cv.ml.KNearest_create()
knn.train(trainData, cv.ml.ROW_SAMPLE, response)
ret, results, neighbours ,dist = knn.findNearest(newcomer, 3)
print( "result:  {}\n".format(results) )
print( "neighbours:  {}\n".format(neighbours) )
print( "distance:  {}\n".format(dist) )

plt.show() 