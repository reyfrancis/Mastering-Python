''' Recording a Video '''

import numpy as np
import cv2
import sys

cap = cv2.VideoCapture(0)

# Check if the OS is Windows or Linux
if sys.platform == 'win32':
    PATH_sys = 'C:/Users/Joelatech24'
elif sys.platform == 'linux':
    PATH_sys = '/home/rey'

# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter(PATH_sys + '/Desktop/Mastering-Python/OpenCV/Image Files/output.avi',fourcc, 20.0, (640,480))   # Last argument is (width, height)

while(cap.isOpened()):
    ret, frame = cap.read()
    if ret==True:
        frame = cv2.flip(frame,0)   # Flip upside down the video

        out.write(frame)   # write the video

        cv2.imshow('frame',frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

# Release everything if job is finished
cap.release()
out.release()
cv2.destroyAllWindows()
