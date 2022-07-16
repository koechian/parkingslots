import cv2
from pathlib import Path
import numpy as np

cap = cv2.imread(str(Path("data/overhead_parking.png")))


while True:
    disp = cv2.GaussianBlur((cv2.cvtColor(cap, cv2.COLOR_BGR2GRAY)), (3, 3), 1)

    threshold = cv2.adaptiveThreshold(
        disp, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 25, 16
    )
    median = cv2.medianBlur(threshold, 5)

    kernels = np.ones((3, 3), np.uint8)

    dilate = cv2.dilate(median, kernels, iterations=1)

    cv2.imshow("Feed", dilate)

    key = cv2.waitKey(1)

    if key == 27:
        break
