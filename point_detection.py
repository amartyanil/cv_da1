import cv2
from kernels import *

img = cv2.imread("points.png",cv2.IMREAD_GRAYSCALE)
detected_points = cv2.filter2D(src=img,ddepth=-1,kernel=point_detection_kernel)
cv2.imshow("Points",detected_points)
cv2.waitKey(0)

cv2.destroyAllWindows()