#import numpy as np
import cv2

cap = cv2.VideoCapture(0) #Video can be convert into sequences of Images with Fps( Frame Per Second)
while(True):# Cap.isopened()

# Capture frame-by-frame
    HasFrame,ImgX = cap.read() # Has Frame Has True and False Value
# Our operations on the frame come here
    hsv = cv2.cvtColor(ImgX, cv2.COLOR_BGR2HSV) # HSV Color conversion
    Gray = cv2.cvtColor(ImgX, cv2.COLOR_BGR2GRAY) # Gray Scale conversion

# Display the resulting frame
    cv2.imshow('ImgX',ImgX) # ImgX Window
    cv2.imshow('hsv', hsv) # HSV Window
    cv2.imshow('gray', Gray) # Gray Window

    if cv2.waitKey(1) & 0xFF == ord('q'): # Remember Must used Q to stopped the scene , 1 is passed for infinite  time
        break
# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()



