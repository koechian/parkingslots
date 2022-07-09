import numpy as np
import cv2 as cv
import scipy.ndimage as ndi

img = cv.imread("Assets/overhead_parking.png")
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
smooth = ndi.median_filter(gray, size=2)
edges = cv.Canny(gray, 100, 150)


while True:
    # for x in lines:
    #     for rho, theta in x:
    #         # print(rho, theta)
    #         a = np.cos(theta)
    #         b = np.sin(theta)
    #         x0 = a * rho
    #         y0 = b * rho
    #         x1 = int(x0 + 1000 * (-b))
    #         y1 = int(y0 + 1000 * (a))
    #         x2 = int(x0 - 1000 * (-b))
    #         y2 = int(y0 - 1000 * (a))

    #         cv.line(img, (x1, y1), (x2, y2), (0, 0, 255), 2)
    #         cv.imshow("Grayscale", img)

    # cv.imshow("Smooth", smooth)
    cv.imshow("edges", edges)
    # cv.imshow("Original", img)

    key = cv.waitKey(1)

    if key == 27:
        break
# Show the result
# cv.imshow("Line Detection", img)
cv.destroyAllWindows()
