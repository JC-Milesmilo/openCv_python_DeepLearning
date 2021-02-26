import numpy as np
import cv2 as cv

face_cascade = cv.CascadeClassifier('C:/SisteProjects/ML/OpenCv/faceRecognition/DevEnv/Lib/site-packages/cv2/data/haarcascade_frontalface_alt2.xml')

print(face_cascade)

cap = cv.VideoCapture(0)

while True:
    #capture frame
    ret, frame = cap.read()

    #if frame doesn't works
    if not ret:
        print("Can't receive frame")
        break
    #put gray scale
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.5, minNeighbors=5)
    for (x,y,w,h) in faces:
        print(x,y,w,h)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]

        #recognize deep learned model predict

        img_item= "imgs/my-image.png"
        cv.imwrite(img_item, roi_gray)

        #draw a rectangle
        color = (255,0,0)
        stroke = 2
        end_cord_width_x = x + y
        end_cord_height_y = y + h
        cv.rectangle(frame,(x,y), (end_cord_width_x, end_cord_height_y), color, stroke)
    #display
    cv.imshow("frame", frame)
    if cv.waitKey(1) == ord('q'):
        break
# when finish well
#cap.realese()
#cv.destroyAllwindows()