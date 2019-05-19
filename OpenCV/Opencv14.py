''' Add Image without Overlap and MASK '''

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


#--------------------------------BLACK BACKGROUND--------------
# Load two images
img1 = cv2.imread(PATH_sys + '/Desktop/Mastering-Python/OpenCV/Image Files/messi.jpg')
img2 = cv2.imread(PATH_sys + '/Desktop/Mastering-Python/OpenCV/Image Files/opencv_black.png')

rows,cols,channels = img2.shape   # We define the img2 pixels
roi = img1[0:rows, 0:cols ]   # We take the img1 rectangle from the top left in the shape of image 2.
# 'roi' is an image taken from the image1 top left in the size of image 2. This will be use later for cv2.bitwise_and()


cv2.imshow('roi', roi)
cv2.waitKey(0)
cv2.destroyAllWindows()


# Convert the image to gray
img2gray= cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
cv2.imshow('Convert to Gray', img2gray)
cv2.waitKey(0)
cv2.destroyAllWindows()

'''
Use global value threshold
cv2.threshold(img, threshold_value, output_value, threshold_style)

Take note that its absurd at its seems since, both black and white require three channels, that is B value, G value, and R value.
But for the sake of simplicity, here we use: 0 = BLACK, 255 = WHITE.

What happens under the hood here is that we check:

if pixel_value > threshold_value:
    pixel_value = output value.
else:
    # leave as it is


So analyzing step by step. Say we use a black background image. Then we will convert all the necessary pixels into WHITE, that is, 
ouput_value = 255

Then we set a threshold, that is whiter than black. Say we use 200.

And so going back. 
If pixel_value is darker that 200:
    pixel_value is equal to white

OR if the background image is BLACK, we just use BLACK as the threshold. Which means


If pixel_value is darker that BLACK:
    pixel_value is equal to white
'''

# Important note: 'mask' will serve as the selection for cv2.bitwise_and()
# 'mask' is the region of WANTED pixels or the white pixels
ret, mask = cv2.threshold(img2gray, 0, 255, cv2.THRESH_BINARY)
cv2.imshow('Apply Threshold', mask)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Inverse the color, that is, the WANTED pixels or 'mask' will now become black
# and the BLACK background will become white
mask_inv = cv2.bitwise_not(mask)
cv2.imshow('Inverse Image', mask_inv)
cv2.waitKey(0)
cv2.destroyAllWindows()


'''
Notice that we have 3 input images to be added. That is,
img1_bg = cv2.bitwise_and(input_img1, input_img2, mask=input_img3)
And input_img1 == input_img2.

The basic concept behind this is the color WHITE background of 'mask_inv' will be added to the 'roi' image. 
Since WHITE + anycolor = anycolor. Then it will make the illusion of removing the white color and changing it with the 'roi' image.

And the Black will remain as it is.
'''
img1_bg = cv2.bitwise_and(roi, roi, mask=mask_inv)
cv2.imshow('Add White background with roi', img1_bg)
cv2.waitKey(0)
cv2.destroyAllWindows()


'''
Here, we will add image2 with the 'mask'. Remember that the 'mask' was not yet inverted, and so the WANTED pixels are colored
white while the rest are colored BLACK.

WHITE + image2 = image2

That is, we just get all WANTED pixels from the image 2 and leave the BLACK as it is. 
'''
img2_fg = cv2.bitwise_and(img2 , img2, mask=mask)
cv2.imshow('Get only ROI', img2_fg)
cv2.waitKey(0)
cv2.destroyAllWindows()


'''
Here, it is important to take note. That using cv2.add() is not the same by adding images using cv2.bitwise_and()

BLACK does have a value of 0. 
So using cv2.add(), BLACK + anycolor = anycolor 
'''
dst = cv2.add(img1_bg, img2_fg)
img1[0:rows, 0:cols ] = dst
cv2.imshow('res', img1)
cv2.waitKey(0)
cv2.destroyAllWindows()





#--------------------------------WHITE BACKGROUND--------------
img1 = cv2.imread(PATH_sys + '/Desktop/Mastering-Python/OpenCV/Image Files/messi.jpg')
img2 = cv2.imread(PATH_sys + '/Desktop/Mastering-Python/OpenCV/Image Files/opencv_white.png')


rows,cols,channels = img2.shape   
roi = img1[0:rows, 0:cols ]   


cv2.imshow('roi', roi)
cv2.waitKey(0)
cv2.destroyAllWindows()


# Convert the image to gray
img2gray= cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
cv2.imshow('Convert to Gray', img2gray)
cv2.waitKey(0)
cv2.destroyAllWindows()


'''
So analyzing step by step. Since we have a WHITE background. Then we will convert all the necessary pixels into BLACK, that is, 
ouput_value = 0

OR

We could just apply INVERSE before doing anything. Then we set a threshold, that is whiter than black. Say we use 200.

And so going back. 
If pixel_value is darker that 200:
    pixel_value is equal to white

OR if the background image is BLACK, we just use BLACK as the threshold. Which means


If pixel_value is darker that BLACK:
    pixel_value is equal to white
'''
img2gray = cv2.bitwise_not(img2gray)
cv2.imshow('Inverse Image', img2gray)
cv2.waitKey(0)
cv2.destroyAllWindows()


ret, mask = cv2.threshold(img2gray, 0, 255, cv2.THRESH_BINARY)
cv2.imshow('Apply Threshold', mask)
cv2.waitKey(0)
cv2.destroyAllWindows()

mask_inv = cv2.bitwise_not(mask)
cv2.imshow('Inverse Image', mask_inv)
cv2.waitKey(0)
cv2.destroyAllWindows()

img1_bg = cv2.bitwise_and(roi, roi, mask=mask_inv)
cv2.imshow('Add White background with roi', img1_bg)
cv2.waitKey(0)
cv2.destroyAllWindows()

img2_fg = cv2.bitwise_and(img2 , img2, mask=mask)
cv2.imshow('Get only ROI', img2_fg)
cv2.waitKey(0)
cv2.destroyAllWindows()

dst = cv2.add(img1_bg, img2_fg)
img1[0:rows, 0:cols ] = dst
cv2.imshow('res', img1)
cv2.waitKey(0)
cv2.destroyAllWindows()