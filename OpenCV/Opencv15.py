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
import cv2 
import numpy as np
from matplotlib import pyplot as plt

# cv.threshold(img, threshold_value, output_value, threshold_style)
img = cv2.imread('C:/Users/Joelatech24/Desktop/Mastering-Python/OpenCV/Image Files/gradient.png', 0)

ret,thresh1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
ret,thresh2 = cv2.threshold(img,127,255,cv2.THRESH_BINARY_INV)
ret,thresh3 = cv2.threshold(img,127,255,cv2.THRESH_TRUNC)
ret,thresh4 = cv2.threshold(img,127,255,cv2.THRESH_TOZERO)
ret,thresh5 = cv2.threshold(img,127,255,cv2.THRESH_TOZERO_INV)

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

for i in range(6):
	plt.subplot(2, 3, i+1) 
	plt.imshow(images[i], 'gray')
	plt.title(titles[i])
	plt.xticks([]), plt.yticks([])   # Hide the x and y axis
plt.show()

''' 
Closing matplotlib window:

plt.close()   # will close current instance.
plt.close(2)   # will close figure 2
plt.close(plot1)   # will close figure with instance plot1
plt.close('all')   # will close all fiures 
'''

# PRESS Q to close

'''
plt.show() is a blocking function.

Essentially, if you want two windows to open at once, you need to create two figures, and then use plt.show() at the end to 
display them. In fact, a general rule of thumb is that you set up your plots, and plt.show() is the very last thing you do.

So in your case:

fig1 = plt.figure(figsize=plt.figaspect(0.75))
ax1 = fig1.add_subplot(1, 1, 1)
im1, = plt.imshow(eye(3))

fig2 = plt.figure(figsize=plt.figaspect(0.75))
ax2 = fig2.add_subplot(1, 1, 1)
im2, = plt.imshow(eye(2))

plt.show()
You can switch between the plots using axes(ax2).

I put together a comprehensive example demonstrating why the plot function is blocking and how it can be used in an answer to 
another question: 
'''


# ---------------------------------------
'''
Adaptive Thresholding:
In the previous section, we used a global value as threshold value. But it may not be good in all the conditions where image has 
different lighting conditions in different areas. In that case, we go for adaptive thresholding. In this, the algorithm calculate 
the threshold for a small regions of the image. So we get different thresholds for different regions of the same image and it gives
us better results for images with varying illumination.


Adaptive Method - It decides how thresholding value is calculated.
cv2.ADAPTIVE_THRESH_MEAN_C : threshold value is the mean of neighbourhood area.
cv2.ADAPTIVE_THRESH_GAUSSIAN_C : threshold value is the weighted sum of neighbourhood values where weights are a gaussian window.
Block Size - It decides the size of neighbourhood area.

C - It is just a constant which is subtracted from the mean or weighted mean calculated.

adaptiveThreshold(src, dst, maxValue, adaptiveMethod, thresholdType, blockSize, C):

src – Source 8-bit single-channel image.
dst – Destination image of the same size and the same type as src .
maxValue – Non-zero value assigned to the pixels for which the condition is satisfied. See the details below.
adaptiveMethod – Adaptive thresholding algorithm to use, ADAPTIVE_THRESH_MEAN_C or ADAPTIVE_THRESH_GAUSSIAN_C . See the details below.
thresholdType – Thresholding type that must be either THRESH_BINARY or THRESH_BINARY_INV .
blockSize – Size of a pixel neighborhood that is used to calculate a threshold value for the pixel: 3, 5, 7, and so on.
C – Constant subtracted from the mean or weighted mean (see the details below). Normally, it is positive but may be zero or negative as well.
'''

img_adapt = cv2.imread('C:/Users/Joelatech24/Desktop/Mastering-Python/OpenCV/Image Files/dave.jpg', 0)
img_adapt = cv2.medianBlur(img_adapt, 5)

ret,th1 = cv2.threshold(img_adapt, 127, 255, cv2.THRESH_BINARY)
th2 = cv2.adaptiveThreshold(img_adapt, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)
th3 = cv2.adaptiveThreshold(img_adapt, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)

titles_adapt = ['Original Image', 'Global Thresholding (v = 127)',
            'Adaptive Mean Thresholding', 'Adaptive Gaussian Thresholding']
images_adapt = [img_adapt, th1, th2, th3]

for i in range(4):
    plt.subplot(2, 2, i+1)
    plt.imshow(images_adapt[i], 'gray')
    plt.title(titles_adapt[i])
    plt.xticks([]),plt.yticks([])
plt.show()

