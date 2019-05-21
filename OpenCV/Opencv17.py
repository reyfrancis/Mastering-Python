'''
There are more than 150 color-space conversion methods available in OpenCV. But we will look into only two which are most 
widely used ones, BGR -> Gray and BGR -> HSV.

For color conversion, we use the function cv2.cvtColor(input_image, flag) where flag determines the type of conversion.

For BGR -> Gray conversion we use the flags cv2.COLOR_BGR2GRAY. Similarly for BGR -> HSV, we use the flag cv2.COLOR_BGR2HSV. 
To get other flags, just run following commands in your Python terminal:
'''

# Declare libraries
import cv2 
import numpy as np
from matplotlib import pyplot as plt
import sys


flags = [i for i in dir(cv2) if i.startswith('COLOR_')]
print(flags)

'''
Note: For HSV, Hue range is [0,179], Saturation range is [0,255] and Value range is [0,255]. Different softwares use different 
scales. So if you are comparing OpenCV values with them, you need to normalize these ranges. 
'''

cap = cv2.VideoCapture(0)

while(1):

    # Take each frame
    _, frame = cap.read()

    # Convert BGR to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # define range of blue color in HSV
    lower_blue = np.array([110,50,50])
    upper_blue = np.array([130,255,255])

    # Threshold the HSV image to get only blue colors
    mask = cv2.inRange(hsv, lower_blue, upper_blue)

    # Bitwise-AND mask and original image
    res = cv2.bitwise_and(frame,frame, mask= mask)

    cv2.imshow('frame',frame)
    cv2.imshow('mask',mask)
    cv2.imshow('res',res)
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()
