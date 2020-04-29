import numpy as np
import cv2 as cv
face_cascade = cv.CascadeClassifier('/home/oem/opencv/data/haarcascades/haarcascade_russian_plate_number.xml')
#eye_cascade = cv.CascadeClassifier('Z:\Dev\Anaconda\pkgs\libopencv-3.4.1-h875b8b8_3\Library\etc\haarcascades\haarcascade_eye.xml')
img = cv.imread('test.jpg')
#hsv = cv.cvtColor(img, cv.COLOR_BGR2SV)
hsv=cv.imread('test.jpg',0)
#russian plates work best
faces = face_cascade.detectMultiScale(hsv, 1.3, 5)
counter = 1
for (x,y,w,h) in faces:
     temp = img[y: y + h, x: x + w]
     cv.imwrite("plates/plate"+str(counter)+".jpg",temp)
     cv.rectangle(img,(x,y),(x+w,y+h),(0, 100, 0),5)
     roi_gray = hsv[y:y+h, x:x+w]
     roi_color = img[y:y+h, x:x+w]
     counter+=1
    
cv.imshow('img',img)
cv.waitKey(0)
cv.destroyAllWindows()
