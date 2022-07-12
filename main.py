import numpy as np
import pickle
import cv2
import cvzone

from pathlib import Path
from slots import *

with open("slots.p", "rb") as f:
    nodePos = pickle.load(f)

VIDEO_LOCATION = str(Path("data/overhead_parking.mp4"))


def process(feed):

    # the image has been converted to grayscale and blurred
    processed = cv2.GaussianBlur((cv2.cvtColor(feed, cv2.COLOR_BGR2GRAY)), (3, 3), 1)

    # converting to binary image map
    threshold = cv2.adaptiveThreshold(
        processed, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 25, 16
    )

    # applying median blur to reduce noise
    median = cv2.medianBlur(threshold, 5)

    # stretching the pixels in the image to make it easier to find bounds

    kernels = np.ones((3, 3), np.uint8)
    dilate = cv2.dilate(median, kernels, iterations=1)
    return dilate


def checkSlot(processed):
    for nd in nodePos:
        x, y = nd
        slot = processed[y : y + HEIGHT, x : x + WIDTH]

        cv2.imshow(str(x * y), slot)

        # counting all non-zero pixels
        count = cv2.countNonZero(slot)
        cvzone.putTextRect(
            feed, str(count), (x, y + HEIGHT - 10), scale=1, thickness=2, offset=0
        )


cap = cv2.VideoCapture(VIDEO_LOCATION)

while True:
    # looping the video
    if cap.get(cv2.CAP_PROP_POS_FRAMES) == cap.get(cv2.CAP_PROP_FRAME_COUNT):
        cap.set(cv2.CAP_PROP_POS_FRAMES, 0)

    _, feed = cap.read()

    # image processing
    checkSlot(process(feed))

    for x in nodePos:
        cv2.rectangle(feed, x, (x[0] + WIDTH, x[1] + HEIGHT), [0, 255, 0], 2)

    cv2.imshow("Video Feed", feed)
    # cv2.imshow("Processed", process(feed))

    cv2.waitKey(10)
