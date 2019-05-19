''' Basic Operation on Images '''

import cv2 
import numpy as np
import sys

# Check if the OS is Windows or Linux
if sys.platform == 'win32':
    PATH_sys = 'C:/Users/Joelatech24'
elif sys.platform == 'linux':
    PATH_sys = '/home/rey'

img = cv2.imread(PATH_sys + '/Desktop/Mastering-Python/OpenCV/Image Files/Rose.jpeg', cv2.IMREAD_COLOR)
cv2.imshow('Rose RED', img)

# Say we want to know what is the color or pixel value of a certain pixel
px = img[100, 100]
print(px)

# Remember that: img[Column, Row, index] is the complete argument, index can be 0, 1 or 2
# 0 = Blue, 1 = Green, 2 = Blue

# Say we want to get the intensity of BLUE, then
blue_intensity = img[100, 100, 0]

# or we want to get the GREEN intensity
green_intensity = img[100, 100, 1]

# and lastly the RED
red_intensity = img[100, 100, 2]

# And we can see that indeed they are the same
print(img[100, 100])
print([blue_intensity, green_intensity, red_intensity])

# To modify the pixels
img[100,100] = [255,255,255]



'''
Above mentioned method is normally used for selecting a region of array, 
say first 5 rows and last 3 columns like that. For individual pixel access, 
Numpy array methods, array.item() and array.itemset() is considered to be better. 
But it always returns a scalar. So if you want to access all B,G,R values, you need 
to call array.item() separately for all.
'''

# Accessing RED intensity
print(img.item(100, 100, 2))


# Modifying RED value
img.itemset((10, 10, 2), 100)



# Say we want to change the color of the Black Quora logo to Red
img_quora = cv2.imread(PATH_sys + '/Desktop/Mastering-Python/OpenCV/Image Files/quora.png', cv2.IMREAD_COLOR)
cv2.imshow('Black Quora', img_quora)

# Our approach is to get the color profile of the BLACK Quora
# Then we change all the color profile of BLACK with the RED one.

black_profile = img_quora[110, 165]   # Just pick a point in the image where it is black


print(type(black_profile))   # Since both black_profile is numpy.ndarray
print(black_profile)   # And its values are separated by spaces and not commas
black_list = list(black_profile)   # We will turn this into a list and them so that it will be separated by comma
print(black_list)   # To verify it is already a list

#OR

# b,g,r = cv2.split(img)
# img = cv2.merge((b,g,r))
# print(img)

# Save inside an array all the pixels for which the image has BLACK profile
indices = np.where((img_quora == black_list))

'''
It is important to note that the value we get in indices or the indices list will be like this:

print(indices) = 
[0, 0, 0, 1, 1, 1, 2, 2, 2, . . .],   # This will correspond to the columns
[0, 0, 0, 1, 1, 1, 2, 2, 2, . . .],   # This will correspond to the rows
[0, 1, 2, 0, 1, 2, 0, 1, 2, . . .]    # This will correspond to the color

Which means that every single pixel will be represented by 3 values in columns, in rows, and in color.
'''
i = 0
while i < len(indices[0]) :
    img_quora.itemset((indices[0][i], indices[1][i], 0), 0)
    img_quora.itemset((indices[0][i], indices[1][i], 1), 0)
    img_quora.itemset((indices[0][i], indices[1][i], 2), 255)
    i+=3   # Since each pixel will be repeated 3 times, for its Red, Green, and Blue color.
           # We need to iterate by 3's

cv2.imwrite(PATH_sys + '/Desktop/Mastering-Python/OpenCV/Image Files/Output.jpg', img_quora)
img_quora_red = cv2.imread(PATH_sys + '/Desktop/Mastering-Python/OpenCV/Image Files/Output.jpg', cv2.IMREAD_COLOR)
cv2.imshow('Red Quora', img_quora_red)

cv2.waitKey(0)
cv2.destroyAllWindows()
