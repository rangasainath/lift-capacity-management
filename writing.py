import numpy as np
import cv2 as cv
cap=cv.VideoCapture(0)
fourcc=cv.VideoWriter_fourcc(*'mp4v')
out=cv.VideoWriter('myvideo.mp4',fourcc,20.0,(640,480))
while(cap.isOpened()):
    ret,frame=cap.read()
    if(ret==True):
        out.write(frame)
        cv.imshow('output',frame)
        if(cv.waitKey(1) & 0xFF ==ord('q')):
            break
    else:
        break
cap.release()
cv.destroyAllWindows()