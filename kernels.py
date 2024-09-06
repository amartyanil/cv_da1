import cv2
import numpy as np

point_detection_kernel = np.array([[-1,-1,-1],[-1,8,-1],[-1,-1,-1]])
line_horizontal_detection_kernel = np.array([[-1,-1,-1],[-2,-2,-2],[-1,-1,-1]])
line_vertical_detection_kernel = np.array([[-1,-2,-1],[-1,-2,-1],[-1,-2,-1]])
line_45_detection_kernel = np.array([[-1,-1,-2],[-1,-2,-1],[-2,-1,-1]])
line_135_detection_kernel = np.array([[-2,-1,-1],[-1,-2,-1],[-1,-1,-2]])
sobelx_kernel = np.array([[-1,-2,-1],[0,0,0],[1,2,1]])
sobely_kernel = np.array([[-1,0,1],[-2,0,2],[-1,0,1]])
prewittx_kernel = np.array([[-1,-1,-1],[0,0,0],[1,1,1]])
prewitty_kernel = np.array([[-1,0,1],[-1,0,1],[-1,0,1]])
robertx_kernel = np.array([[-1,0],[0,1]])
roberty_kernel = np.array([[0,-1],[1,0]])
