import numpy as np
import cv2
from kernels import *

img = cv2.imread("room.png",cv2.IMREAD_GRAYSCALE)

#rober edge detection
robert_x = cv2.filter2D(src=img,ddepth=-1,kernel=robertx_kernel)
cv2.imshow("Robert's Gradient Applied on the X-axis",robert_x)
cv2.waitKey(0)
robert_y = cv2.filter2D(src=img,ddepth=-1,kernel=roberty_kernel)
cv2.imshow("Robert's Gradient Applied on the Y-axis",robert_y)
cv2.waitKey(0)
robert_magnitude = np.sqrt(np.float32(robert_x) ** 2 + np.float32(robert_y) ** 2)
robert_magnitude_normalized = cv2.normalize(robert_magnitude, None, 0, 255, cv2.NORM_MINMAX)
robert_magnitude_normalized = np.uint8(robert_magnitude_normalized)
cv2.imshow("Robert's Gradient Magnitudes",robert_magnitude_normalized)
cv2.waitKey(0)

#prewitt edge detection
prewitt_x = cv2.filter2D(src=img,ddepth=-1,kernel=prewittx_kernel)
cv2.imshow("Prewitt Filter Applied on the X-axis",prewitt_x)
cv2.waitKey(0)
prewitt_y = cv2.filter2D(src=img,ddepth=-1,kernel=prewitty_kernel)
cv2.imshow("Prewitt Filter Applied on the Y-axis",prewitt_y)
cv2.waitKey(0)
prewitt_magnitude = np.sqrt(np.float32(prewitt_x) ** 2 + np.float32(prewitt_y) ** 2)
prewitt_magnitude_normalized = cv2.normalize(prewitt_magnitude, None, 0, 255, cv2.NORM_MINMAX)
prewitt_magnitude_normalized = np.uint8(prewitt_magnitude_normalized)
cv2.imshow("Prewitt Filter Magnitudes",prewitt_magnitude_normalized)
cv2.waitKey(0)

cv2.destroyAllWindows()