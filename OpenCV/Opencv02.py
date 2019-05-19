''' Viewing and writing Image using matplotlib '''

# Import libraries
import numpy as np
import cv2
from matplotlib import pyplot as plt
from matplotlib.pyplot import figure
import sys


# Check if the OS is Windows or Linux
if sys.platform == 'win32':
    PATH_sys = 'C:/Users/Joelatech24'
elif sys.platform == 'linux':
    PATH_sys = '/home/rey'

# Read using opencv
img = cv2.imread(PATH_sys + '/Desktop/Mastering-Python/OpenCV/Image Files/Flower.jpg', cv2.IMREAD_GRAYSCALE)

# figure(figsize=(1,1)) would create an inch-by-inch image, which would be 80-by-80 pixels 
# unless you also give a different dpi argument.
plt.figure(figsize=(5, 5))

plt.plot([200,300,400],[100,200,300],'c', linewidth=5)

# Print the image using matplotlib
plt.imshow(img ,cmap = 'gray', interpolation = 'bicubic')

plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
# This hides the x and y axis on the matplotlib

plt.show()