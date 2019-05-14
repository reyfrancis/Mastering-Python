''' Add Image without Overlap and MASK '''

# Declare libraries
import cv2
import numpy as np
from matplotlib import pyplot as plt

# Load two images
img1 = cv2.imread('C:/Users/Joelatech24/Desktop/Mastering-Python/OpenCV/Image Files/messi.jpg')
img2 = cv2.imread('C:/Users/Joelatech24/Desktop/Mastering-Python/OpenCV/Image Files/Flower.jpg')

rows,cols,channels = img2.shape   # We define the img1 pixels
roi = img1[0:rows, 0:cols ]   # We place the img1 starting from the top left of the img2

# Now create a mask of logo and create its inverse mask also
mask = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)

cv2.imshow('Mask Image', mask)

# ret, mask = cv2.threshold(img2gray, 10, 255, cv2.THRESH_BINARY)
# mask_inv = cv2.bitwise_not(mask)

# # Now black-out the area of logo in ROI
# img1_bg = cv2.bitwise_and(roi,roi,mask = mask_inv)

# # Take only region of logo from logo image.
# img2_fg = cv2.bitwise_and(img2,img2,mask = mask)

# # Put logo in ROI and modify the main image
# dst = cv2.add(img1_bg,img2_fg)
# img1[0:rows, 0:cols ] = dst

# cv2.imshow('res',img1)
cv2.waitKey(0)
cv2.destroyAllWindows()