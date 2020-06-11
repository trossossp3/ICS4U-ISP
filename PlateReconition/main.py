import numpy as np
import cv2 as cv

cascade = cv.CascadeClassifier(
    "/home/oem/opencv/data/haarcascades/haarcascade_russian_plate_number.xml"
)

img = cv.imread("test.jpg", 0)
# russian plates work best
plates = cascade.detectMultiScale(img, 1.3, 5)
counter = 1
for (x, y, w, h) in plates:
    temp = img[y : y + h, x : x + w]
    cv.imwrite("plate" + str(counter) + ".jpg", temp)
    cv.rectangle(img, (x, y), (x + w, y + h), (0, 100, 0), 5)
    roi_gray = img[y : y + h, x : x + w]
    roi_color = img[y : y + h, x : x + w]
    counter += 1

cv.imshow("img", img)
cv.waitKey(0)
cv.destroyAllWindows()
