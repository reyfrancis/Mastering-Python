''' Image ROI '''

# Declare Libraries
import cv2 
import numpy as np

# @TODO: Correct the Image PATH to Ubuntu
img = cv2.imread('C:/Users/Joelatech24/Desktop/Mastering-Python/OpenCV/Image Files/messi.jpg', cv2.IMREAD_COLOR)   # Load colored image

'''
As for the first question - 280:340, 330:390 means: get a rectangle that begins at 280th row and 330th column and 
ends at 340th row and 390 column. Another way to put it: it is a rectangle described by 4 vertices whose coordinates 
are: (280,330), (280,390), (340,330), (340,390).
'''
ball = img[280:340, 330:390]   # In other words, A rectangle having opposite corners at P1(280, 330) and P2(340, 390)
img[273	:333, 100:160] = ball  # Take note that we will get an error if the dimensions aren't correct

# width = 340-280 = 60
# height = 390-330 = 60

# width = 333-273 = 60
# height = 390-330 = 60

try:
	img[272	:333, 100:160] = ball
except:
	print('ValueError: could not broadcast input array from the shape . . . ')


cv2.imshow('Messi', img)


cv2.waitKey(0)
cv2.destroyAllWindows()