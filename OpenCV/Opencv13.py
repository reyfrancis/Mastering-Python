''' Add Image with Overlap and Transparency (Weighted Image) '''

# Declare libraries
import cv2
import numpy as np
from matplotlib import pyplot as plt

'''
You can add two images by OpenCV function, cv2.add() or simply by numpy operation, res = img1 + img2. 
Both images should be of same depth and type, or second image can just be a scalar value.
Note There is a difference between OpenCV addition and Numpy addition. OpenCV addition is a saturated operation 
while Numpy addition is a modulo operation.
'''

x = np.uint8([250])
y = np.uint8([10])

cv2.add(x, y)   # 250+10 = 260 => 255

print(x + y)   # 250+10 = 260 % 256 = 4


img1 = cv2.imread('C:/Users/Joelatech24/Desktop/Mastering-Python/OpenCV/Image Files/m1.jpg', cv2.IMREAD_COLOR)
img2 = cv2.imread('C:/Users/Joelatech24/Desktop/Mastering-Python/OpenCV/Image Files/m2.jpg',  cv2.IMREAD_COLOR)

sum_image = cv2.addWeighted(img2, 0.7, img1, 0.3, 0)   # Weighted image is a more formal term to saying transparency of an image
# In order to add two images, they must have the same shape. 

print(img1.shape)
print(img2.shape)

cv2.imshow('Sum', sum_image)
cv2.waitKey(0)
cv2.destroyAllWindows()