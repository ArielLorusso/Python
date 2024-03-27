# https://docs.opencv.org/3.4/db/d5b/tutorial_py_mouse_handling.html

import numpy as np
import cv2
import time
import random

random.seed(42)
Ymax = 720 #480
Xmax = 1080 #640
img = np.zeros((Ymax,Xmax , 3), np.uint8)

x,y=0,0
arrX,arrY = [],[]
for j in range (0,20):
        arrX.append( int((random.randrange(Xmax))/6))
        arrY.append( int((random.randrange(Ymax))/6))

for i in range (0,2000):
    cv2.rectangle(img,(-10,-10),(Xmax,Ymax),(100,0,0),-1)
    x=(x+1)%Xmax
    y=(y+1)%Ymax
    for j in range (0,1):
        cv2.rectangle(img,(x+arrX[j]%Xmax,y+arrY[j]%Ymax),(x+arrX[j]+30%Xmax,y+arrY[j]+30%Ymax),(0,200,200),5)
       # cv2.rectangle(img,(y+arrY[j]%Ymax,x+arrX[j]%Xmax),(y+arrY[j]+30%Ymax,x+arrX[j]+30%Xmax),(0,200,200),5)

    #cv2.circle(img,(x,y), radius=10, color=(143,14,143),thickness=2, lineType=cv2.LINE_AA)
    
    cv2.imshow('CV_Tutorial', img)
    key = cv2.waitKey(1)
    if key & 0xFF == 27:
        break
    if key == 112:          # ASCII 112 = 'p'  https://www.asciitable.com/
        key = 0 
        while  not( key == 112): 
            key = cv2.waitKey(1)
#cv2.destroyAllWindows()