''' Performance Measurement and Improvement Techniques '''

# Declare libraries
import cv2 
import numpy as np
from matplotlib import pyplot as plt
import sys



# Check if the OS is Windows or Linux
if sys.platform == 'win32':
    PATH_sys = 'C:/Users/Joelatech24'
elif sys.platform == 'linux':
    PATH_sys = '/home/rey'

'''
cv2.getTickCount function returns the number of clock-cycles after a reference event 
(like the moment machine was switched ON) to the moment this function is called. So if you call it before and after the function 
execution, you get number of clock-cycles used to execute a function.

cv2.getTickFrequency function returns the frequency of clock-cycles, or the number of clock-cycles per second. So to find the time
of execution in seconds, you can do following:
'''

img1 = cv2.imread(PATH_sys + '/Desktop/Mastering-Python/OpenCV/Image Files/messi.jpg')

e1 = cv2.getTickCount()
for i in range(5, 49, 2):
    img1 = cv2.medianBlur(img1,i)
e2 = cv2.getTickCount()
t = (e2 - e1)/cv2.getTickFrequency()
print(t)