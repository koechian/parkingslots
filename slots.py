import pickle
from pathlib import Path
import cv2
import pickle
import cvzone
import math

WIDTH, HEIGHT = 107, 48
GATE = (42, 13)


try:
    with open("slots.p", "rb") as f:
        nodePos = pickle.load(f)
    with open("compDict.p", "rb") as x:
        Dict = pickle.load(x)
except FileNotFoundError:
    nodePos = []
    Dict = dict()


def mouseCLick(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        nodePos.append((x, y))

    if event == cv2.EVENT_RBUTTONDOWN:
        for i, pos in enumerate(nodePos):
            x1, y1 = pos
            if x1 < x < (x1 + WIDTH) and y1 < y < (y1 + HEIGHT):
                nodePos.pop(i)

    with open("slots.p", "wb") as f:
        pickle.dump(nodePos, f)

    getDistance(nodePos)


def getDistance(nodePos):
    index = []
    index.extend(range(1, len(nodePos)))

    i = 1
    for x in nodePos:

        Dict[i] = {
            "pos": x,
            "distance": abs(math.floor(x[0] + (WIDTH / 2)) - GATE[0])
            + abs((math.floor(x[1] + (HEIGHT / 2)) - GATE[1])),
            "occupied": True,
        }

        if i != 69:
            i = i + 1
        else:
            break

    with open("compDict.p", "rb") as f:
        pickle.dump(Dict, f)


if __name__ == "__main__":
    while True:
        count = 1
        img = cv2.imread(str(Path("data/overhead_parking.png")))

        for x in nodePos:
            cv2.rectangle(img, x, (x[0] + WIDTH, x[1] + HEIGHT), [255, 255, 255], 1)

            # circle in centre
            cv2.circle(
                img,
                (
                    math.floor(x[0] + abs(WIDTH / 2)),
                    math.floor(x[1] + abs(HEIGHT / 2)),
                ),
                5,
                [0, 255, 0],
                -2,
            )

            # lot indexes
            cvzone.putTextRect(
                img,
                str(count),
                (
                    math.floor(abs(x[0] + 5)),
                    math.floor(abs(x[1] + 15)),
                ),
                scale=1,
                thickness=1,
                offset=2,
                colorR=[255, 255, 255],
                colorT=[0, 0, 0],
            )

            # distance to gate
            cvzone.putTextRect(
                img,
                f"Distance: {str(abs(math.floor(x[0] + abs(WIDTH / 2))-GATE[0])+((abs(math.floor(x[1] + abs(HEIGHT / 2))-GATE[1]))))}",
                (
                    math.floor(abs(x[0] + 35)),
                    math.floor(abs(x[1] + 45)),
                ),
                scale=0.7,
                thickness=1,
                offset=2,
                colorR=[255, 255, 255],
                colorT=[0, 0, 0],
            )
            count += 1

        cv2.imshow("out", img)
        cv2.setMouseCallback("out", mouseCLick)

        cv2.waitKey(1)
