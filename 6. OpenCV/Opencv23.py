'''
Image Pyramids

Theory
Normally, we used to work with an image of constant size. But in some occassions, we need to work with images of different 
resolution of the same image. For example, while searching for something in an image, like face, we are not sure at what size 
the object will be present in the image. In that case, we will need to create a set of images with different resolution and 
search for object in all the images. These set of images with different resolution are called Image Pyramids (because when they 
are kept in a stack with biggest image at bottom and smallest image at top look like a pyramid).

There are two kinds of Image Pyramids. 1) Gaussian Pyramid and 2) Laplacian Pyramids

Higher level (Low resolution) in a Gaussian Pyramid is formed by removing consecutive rows and columns in Lower level (higher 
resolution) image. Then each pixel in higher level is formed by the contribution from 5 pixels in underlying level with gaussian 
weights. By doing so, a M \times N image becomes M/2 \times N/2 image. So area reduces to one-fourth of original area. It is 
called an Octave. The same pattern continues as we go upper in pyramid (ie, resolution decreases). Similarly while expanding, 
area becomes 4 times in each level. We can find Gaussian pyramids using cv2.pyrDown() and cv2.pyrUp() functions.
'''
import cv2
import numpy as np
from matplotlib import pyplot as plt
import sys

# Check if the OS is Windows or Linux
if sys.platform == 'win32':
    PATH_sys = 'C:/Users/reyfrancis'
elif sys.platform == 'linux':
    PATH_sys = '/home/rey'

img = cv2.imread(PATH_sys + '/Desktop/Mastering-Python/OpenCV/Image Files/messi.jpg', 0)
lower_reso = cv2.pyrDown(higher_reso)

higher_reso2 = cv2.pyrUp(lower_reso)