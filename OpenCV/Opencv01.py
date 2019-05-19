''' Loading Image in OpenCv.
For more details: https://docs.opencv.org/3.0-beta/doc/py_tutorials/py_gui/py_image_display/py_image_display.html 
'''

# Import libraries
import cv2
import numpy as np
from matplotlib import pyplot as plt
import sys

# Use the function cv2.imread(Image, Parameter) to read an image. 
# The 'Image' should be in the working directory or a full path of image should be given.
# Second argument or 'Parameter' is a flag which specifies the way image should be read.

'''
List of Second Argument

cv2.IMREAD_COLOR : Loads a color image. Any transparency of image will be neglected. It is the default flag.
cv2.IMREAD_GRAYSCALE : Loads image in grayscale mode
cv2.IMREAD_UNCHANGED : Loads image as such including alpha channel

Note: Instead of these three flags, you can simply pass integers 1, 0 or -1 respectively.

1 = IMREAD_COLOR
2 = IMREAD_GRAYSCALE
3 = IMREAD_UNCHANGED
'''

# Check if the OS is Windows or Linux
if sys.platform == 'win32':
    PATH_sys = 'C:/Users/Joelatech24'
elif sys.platform == 'linux':
    PATH_sys = '/home/rey'

img_1 = cv2.imread(PATH_sys + '/Desktop/Mastering-Python/OpenCV/Image Files/Rose.jpeg', cv2.IMREAD_COLOR)   # Read Image as Color
cv2.imshow('Flower_Color', img_1)  # Display the Image


# Read Image as Grayscale
img_2 = cv2.imread(PATH_sys +  '/Desktop/Mastering-Python/OpenCV/Image Files/Flower.jpg', cv2.IMREAD_GRAYSCALE)

'''
Note: There is a special case where you can already create a window and load image to it later. 
In that case, you can specify whether window is resizable or not. It is done with the function 
cv2.namedWindow(). By default, the flag is cv2.WINDOW_AUTOSIZE. But if you specify flag to be cv2.
WINDOW_NORMAL, you can resize window. It will be helpful when image is too large in dimension and 
adding track bar to windows. 
'''
cv2.namedWindow('Flower_Gray', cv2.WINDOW_NORMAL)   # The first argument should have the same name 
                                                               # as the first argument of imshow() below.
# Display the Image
cv2.imshow('Flower_Gray', img_2)


''' 
cv2.waitKey(Parameters) is a keyboard binding function. Its argument is the time in milliseconds. 
The function waits for specified milliseconds for any keyboard event. If you press any key 
in that time, the program continues. If 0 is passed, it waits indefinitely for a key stroke. 
It can also be set to detect specific key strokes like, if key a is pressed etc which we will 
discuss below. 

Parameters: delay – Delay in milliseconds. 0 is the special value that means “forever”.

Warning: If you are using a 64-bit machine, you will have to modify k = cv2.waitKey(0) line as follows : 
k = cv2.waitKey(0) & 0xFF 
'''


# We should encapsulate the whole waiting process in a while loop. If we try do like this:
'''
k = cv2.waitKey(0) 
if k & 0xFF == 27:
    cv2.destroyAllWindows()
elif elif k & 0xFF == 32:
    cv2.destroyWindow('Flower_Color')
elif k & 0xFF == ord('s'):
    cv2.imwrite('/home/rey/Desktop/Open-cv/Image Files/Flower_Gray.jpg',img_2)
'''
# We'll see that any key stroke will close all other windows.

while(True):
    k = cv2.waitKey(1)
    if k & 0xFF == 27:   # 27 stands for ESC character
                  # The ASCII "escape" character (octal: \033, hexadecimal: \x1B, or ^[, or, in decimal, 27)
        break

    elif k & 0xFF == 32: # 32 stands for space
        cv2.destroyWindow('Flower_Color')

    elif k & 0xFF == ord('s'): # wait for 's' key
        cv2.imwrite(PATH_sys + '/Desktop/Mastering-Python/OpenCV/Image Files/Flower_Gray.jpg', img_2)
        break

cv2.destroyAllWindows()
'''
cv2.destroyAllWindows() simply destroys all the windows we created. If you want to destroy any 
specific window, use the function cv2.destroyWindow() where you pass the exact window name as 
the argument.
''' 