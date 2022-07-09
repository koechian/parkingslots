import numpy as np
import cv2 as cv
import scipy.ndimage as ndi


def process(image):
    lower = np.uint8([120, 120, 120])
    upper = np.uint8([255, 255, 255])
    white_mask = cv.inRange(image, lower, upper)
    # yellow color mask
    lower = np.uint8([190, 190, 0])
    upper = np.uint8([255, 255, 255])
    yellow_mask = cv.inRange(image, lower, upper)
    # combine the mask
    mask = cv.bitwise_or(white_mask, yellow_mask)
    masked = cv.bitwise_and(image, image, mask=mask)

    # convert to grayscale
    gray = cv.cvtColor(masked, cv.COLOR_RGB2GRAY)

    # detect edges using Canny Method then straight lines using Hough Lines Probablistic
    lines = cv.HoughLinesP(
        (cv.Canny(image, 50, 200)),
        rho=0.1,
        theta=np.pi / 10,
        threshold=130,
        maxLineGap=5,
        minLineLength=6,
    )

    # draw the lines on a copy of the image

    new_img = np.copy(image)
    lines_list = []

    for points in lines:
        x, y, x1, y1 = points[0]
        cv.line(new_img, (x, y), (x1, y1), (0, 0, 255), 2)

        lines_list.append([(x, y), (x1, y1)])

    return new_img


# MAIN
image = cv.imread("Assets/overhead_parking.png")
# image = cv.imread("Assets/overhead_parking.png")


while True:
    cv.imshow("Processed", process(image))

    key = cv.waitKey(1)

    if key == 27:
        break


cv.destroyAllWindows()
