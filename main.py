import pickle
from pathlib import Path
import cv2
import pickle

WIDTH, HEIGHT = 107, 48

try:
    with open("slots.p", "rb") as f:
        nodePos = pickle.load(f)
except:
    nodePos = []


def mouseCLick(event, x, y, flags, params):
    if event == cv2.EVENT_LBUTTONDOWN:
        nodePos.append((x, y))

    if event == cv2.EVENT_RBUTTONDOWN:
        for i, pos in enumerate(nodePos):
            x1, y1 = pos
            if x1 < x < (x1 + WIDTH) and y1 < y < (y1 + HEIGHT):
                nodePos.pop(i)

    with open("slots.p", "wb") as f:
        pickle.dump(nodePos, f)


while True:
    img = cv2.imread(str(Path("data/overhead_parking.png")))

    for x in nodePos:
        cv2.rectangle(img, x, (x[0] + WIDTH, x[1] + HEIGHT), [0, 255, 0], 2)

    cv2.imshow("out", img)
    cv2.setMouseCallback("out", mouseCLick)
    cv2.waitKey(1)
