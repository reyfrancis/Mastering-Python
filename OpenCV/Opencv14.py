''' Add Image without Overlap and MASK '''

# Declare libraries
import cv2
import numpy as np
from matplotlib import pyplot as plt

# Load two images
img1 = cv2.imread('C:/Users/Joelatech24/Desktop/Mastering-Python/OpenCV/Image Files/messi.jpg')
img2 = cv2.imread('C:/Users/Joelatech24/Desktop/Mastering-Python/OpenCV/Image Files/google.jpg')

rows,cols,channels = img2.shape   # We define the img1 pixels
roi = img2[0:rows, 0:cols ]   # We place the img1 starting from the top left of the img2

# Convert the image to gray
mask = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

# Display image and named window as 'Mask Image'
cv2.imshow('Mask Image', mask)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Use global value threshold
ret, mask = cv2.threshold(mask, 220, 255, cv2.THRESH_BINARY)
cv2.imshow('Mask Image', mask)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Inverse the color, that is, the black becomes white and the white becomes black
mask_inv = cv2.bitwise_not(mask)
cv2.imshow('Mask Image', mask_inv)
cv2.waitKey(0)
cv2.destroyAllWindows()


# Now black-out the area of logo in ROI
img1_bg = cv2.bitwise_and(roi, roi, mask=mask_inv)
cv2.imshow('Mask Image', img1_bg)
cv2.waitKey(0)
cv2.destroyAllWindows()


# Take only region of logo from logo image.
img2_fg = cv2.bitwise_and(img2 , img2, mask=mask)
cv2.imshow('Mask Image', img2_fg)
cv2.waitKey(0)
cv2.destroyAllWindows()


# Put logo in ROI and modify the main image. This is to understand well what is img1_bg and img2_fg
dst = cv2.add(img1_bg, img2_fg)
cv2.imshow('Mask Image', dst)
cv2.waitKey(0)
cv2.destroyAllWindows()

# img1[0:rows, 0:cols ] = img2_fg
# cv2.imshow('res', img1)
# cv2.waitKey(0)
# cv2.destroyAllWindows()