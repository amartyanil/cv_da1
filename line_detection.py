import cv2
from kernels import *

img = cv2.imread("pts.png",IMREAD_GRAYSCALE)
detected_lines_horizontal = cv2.filter2D(src=img,ddepth=-1,kernel=line_horizontal_detection_kernel)
detected_lines_vertical = cv2.filter2D(src=img,ddepth=-1,kernel=line_vertical_detection_kernel)
detected_lines_45 = cv2.filter2D(src=img,ddepth=-1,kernel=line_45_detection_kernel)
detected_lines_135 = cv2.filter2D(src=img,ddepth=-1,kernel=line_135_detection_kernel)