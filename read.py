import cv2 as cv
import numpy as np
# Reading images
# img = cv.imread('Resources/Photos/cat.jpg')

# cv.imshow('Cat',img)
# cv.waitKey(0)




# Reading videos
capture = cv.VideoCapture('Resources/Videos/dog.mp4')
while True:
    isTrue,frame = capture.read()
    cv.imshow('Dog',frame)
    if cv.waitKey(20) & 0xFF == ord('d'):
        break

capture.release()
cv.destroyAllWindows()

