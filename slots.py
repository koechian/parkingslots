import cv2 as cv
import pickle
import numpy as np

cap = cv.imread("Assets/parking3.jpg")

# cap=cv2.VideoCapture(0)

while True:
    cnv = cv.cvtColor(cap, cv.COLOR_BGR2HSV)

    lower = np.array([131, 99, 79])
    upper = np.array([203, 255, 147])

    mask = cv.inRange(cnv, lower, upper)

    cv.imshow("Frame", cap)
    cv.imshow("Mask", mask)

    key = cv.waitKey(1)

    if key == 27:
        break

cv.destroyAllWindows()
