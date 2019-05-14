''' Thresholding '''

# Thresholding can be Simple thresholding, Adaptive thresholding, Otsu's thresholding etc.

'''
Simple Thresholding
Here, the matter is straight forward. If pixel value is greater than a threshold value, it is assigned one 
value (may be white), else it is assigned another value (may be black). The function used is cv.threshold. 
First argument is the source image, which should be a grayscale image. Second argument is the threshold value 
which is used to classify the pixel values. Third argument is the maxVal which represents the value to be given 
if pixel value is more than (sometimes less than) the threshold value. OpenCV provides different styles of 
thresholding and it is decided by the fourth parameter of the function. Different types are:
'''
# Declare libraries
import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

# cv.threshold(img, threshold_value, output_value, threshold_style)

img = cv.imread('C:/Users/Joelatech24/Desktop/Mastering-Python/OpenCV/Image Files/gradient.jpg', 0)

ret,thresh1 = cv.threshold(img,127,255,cv.THRESH_BINARY)
ret,thresh2 = cv.threshold(img,127,255,cv.THRESH_BINARY_INV)
ret,thresh3 = cv.threshold(img,127,255,cv.THRESH_TRUNC)
ret,thresh4 = cv.threshold(img,127,255,cv.THRESH_TOZERO)
ret,thresh5 = cv.threshold(img,127,255,cv.THRESH_TOZERO_INV)

titles = ['Original Image','BINARY','BINARY_INV','TRUNC','TOZERO','TOZERO_INV']
images = [img, thresh1, thresh2, thresh3, thresh4, thresh5]
'''
subplot(nrows, ncols, index, **kwargs)
subplot(pos, **kwargs)
Either a 3-digit integer or three separate integers describing the position of the subplot. If the three 
integers are nrows, ncols, and index in order, the subplot will take the index position on a grid with
nrows rows and ncols columns. index starts at 1 in the upper left corner and increases to the right.

pos is a three digit integer, where the first digit is the number of rows, the second the number of columns,
and the third the index of the subplot. i.e. fig.add_subplot(235) is the same as fig.add_subplot(2, 3, 5).
Note that all integers must be less than 10 for this form to work.
'''

# @TODO: Study what value is img, plt.show(), plt.subplot()
for i in range(6):
	plt.subplot(2, 3, i+1) 
	plt.imread(images[i], 0)
	plt.imshow(titles[i], images[i])
	plt.xticks([]), plt.yticks([])   # Hide the x and y axis
plt.show()
