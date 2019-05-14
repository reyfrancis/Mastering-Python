''' Accessing Image Properties '''

# Declare Libraries
import cv2 
import numpy as np

# @TODO: Correct the Image PATH to Ubuntu
img = cv2.imread('C:/Users/Joelatech24/Desktop/Mastering-Python/OpenCV/Image Files/Flower.jpg', cv2.IMREAD_COLOR)   # Load colored image

img_gray = cv2.imread('C:/Users/Joelatech24/Desktop/Mastering-Python/OpenCV/Image Files/Flower.jpg', cv2.IMREAD_GRAYSCALE)   # Load grayed image

# To access the shape of the image
print(img.shape)   # Note the it prints a tuple of (rows, column, channels)
				   # 'channels' refers to the number of in the color scheme. For our picture since it is BGR
				   # Then we have blue channel, green channel and red channel. Hence channel = 3.
print(img_gray.shape)   # Here, it only outputs (rows, column) since gray image have to channel for colors

# To access the size of the image
print(img.size)   # Size = row*column*channels
print(img_gray.size)


# To know the image datatype
print(img.dtype)
'''
Note img.dtype is very important while debugging because a large number of errors in OpenCV-Python code is 
caused by invalid datatype.
'''