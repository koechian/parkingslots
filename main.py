import sys
import numpy as np
import pickle
import cv2
import cvzone
from pathlib import Path

# Global vars
VIDEO_LOCATION = str(Path("data/overhead_parking.mp4"))
WIDTH, HEIGHT = 107, 48


try:
    with open("compDict.p", "rb") as x:
        mainDict = pickle.load(x)
        Dict = mainDict
except FileNotFoundError:
    sys.exit("Run Slots.py first to generate slots to watch")


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
    for x in Dict.values():
        a, b = x["pos"]
        slot = processed[b : b + HEIGHT, a : a + WIDTH]

        # counting all non-zero pixels
        count = cv2.countNonZero(slot)

        # showing non-zero pixel count
        # cvzone.putTextRect(
        #     feed, str(count), (a + 10, b + 10), 1, 1, (255, 255, 255), (0, 0, 0)
        # )
        print(Dict)
        if count < 800:
            # change the slot occupancy if empty
            color = [0, 255, 0]
            availableSlots += 1
            thickness = 2
            x["occupied"] = False
            print(Dict)
        else:
            color = [255, 255, 255]
            thickness = 1

        cv2.rectangle(feed, (a, b), (a + WIDTH, b + HEIGHT), color, thickness)

    cvzone.putTextRect(
        feed,
        f"Free:{availableSlots}/{len(Dict)}",
        (50, 50),
        scale=2,
        thickness=1,
        offset=3,
        colorR=[255, 255, 255],
        colorT=[0, 0, 0],
    )


cap = cv2.VideoCapture(VIDEO_LOCATION)

while True:
    count = 1
    # looping the video
    if cap.get(cv2.CAP_PROP_POS_FRAMES) == cap.get(cv2.CAP_PROP_FRAME_COUNT):
        cap.set(cv2.CAP_PROP_POS_FRAMES, 0)

    _, feed = cap.read()
    checkSlot(process(feed))

    for x in Dict.values():
        # lot indexes
        cvzone.putTextRect(
            feed,
            str(count),
            (
                x["pos"][0] + 5,
                x["pos"][1] + 15,
            ),
            scale=1,
            thickness=1,
            offset=2,
            colorR=[255, 255, 255],
            colorT=[0, 0, 0],
        )

        # distance to gate
        cvzone.putTextRect(
            feed,
            f"Distance: {x['distance']}",
            (
                x["pos"][0] + 35,
                x["pos"][1] + 45,
            ),
            scale=0.7,
            thickness=1,
            offset=2,
            colorR=[255, 255, 255],
            colorT=[0, 0, 0],
        )
        count += 1

    # image processing

    cv2.imshow("Parking Lot Feed", feed)

    key = cv2.waitKey(10)

    if key == 27:
        break
