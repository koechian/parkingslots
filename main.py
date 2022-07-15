import numpy as np
import pickle
import cv2
import cvzone

from pathlib import Path
from slots import *

with open("slots.p", "rb") as f:
    nodePos = pickle.load(f)


# creating a list of nums to be used as the dict keys
nums = []
VIDEO_LOCATION = str(Path("data/overhead_parking.mp4"))


def calcDistance(feed):
    pass


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
    availableSlots = 0
    for nd in nodePos:
        x, y = nd
        slot = processed[y : y + HEIGHT, x : x + WIDTH]

        # counting all non-zero pixels
        count = cv2.countNonZero(slot)
        # cvzone.putTextRect(
        #     feed, str(count), (x, y + HEIGHT - 10), scale=1, thickness=2, offset=0
        # )

        if count < 900:
            # append the slot to a dict with [index,distance]
            color = [0, 255, 0]
            availableSlots += 1
            thickness = 2
        else:
            color = [255, 255, 255]
            thickness = 1

        cv2.rectangle(feed, (x, y), (x + WIDTH, y + HEIGHT), color, thickness)
    cvzone.putTextRect(
        feed,
        f"Free:{availableSlots}/{len(nodePos)}",
        (50, 50),
        scale=2,
        thickness=1,
        offset=3,
        colorR=[255, 255, 255],
        colorT=[0, 0, 0],
    )


cap = cv2.VideoCapture(VIDEO_LOCATION)

while True:
    # looping the video
    if cap.get(cv2.CAP_PROP_POS_FRAMES) == cap.get(cv2.CAP_PROP_FRAME_COUNT):
        cap.set(cv2.CAP_PROP_POS_FRAMES, 0)

    _, feed = cap.read()

    # image processing
    checkSlot(process(feed))
    drawGate(feed)

    cv2.imshow("Video Feed", feed)

    cv2.waitKey(10)
