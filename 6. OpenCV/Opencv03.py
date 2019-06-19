''' Using Camera '''

import numpy as np
import cv2

'''
To capture a video, you need to create a VideoCapture object. Its argument can be either the 
device index or the name of a video file. Device index is just the number to specify which camera. 
Normally one camera will be connected (as in my case). So I simply pass 0 (or -1). You can select 
the second camera by passing 1 and so on. After that, you can capture frame-by-frame. But at the end, 
don’t forget to release the capture.
'''
cap = cv2.VideoCapture(0)

while(True):
    # 'frame' will get the next frame in the camera (via "cap"). 'ret' will obtain return value 
    # from getting the camera frame, either true of false. cap.read() returns a bool (True/False). 
    #If frame is read correctly,  it will be True.
    ret, frame = cap.read()   # This code initiates an infinite loop (to be broken later by a break statement

    # If for some reason calling the above code did not initialized the capture. 
    # we can: 
    print(cap.isOpened())
    if cap.isOpened() == False:
        cap.open()

    
    # Say we want to get and change the height and width of the video
    width = cap.get(3) 
    height = cap.get(4)
    print(width, height)

    ret = cap.set(3, 320) 
    ret = cap.set(4, 240)   # Resize to 320, 240


    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Display the resulting frame
    cv2.imshow('frame',gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()