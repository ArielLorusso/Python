# https://www.youtube.com/watch?v=bIeOPYAlcGQ
# https://docs.opencv.org/3.4/db/d5b/tutorial_py_mouse_handling.html
# https://stackoverflow.com/questions/14494101/using-other-keys-for-the-waitkey-function-of-opencv

import numpy as np
import cv2
import random

Ymax = 720; Xmax = 1080
img = np.zeros((Ymax, Xmax, 3), np.uint8)
x,y=0,0

def rand_binary (img ):
    random_numbers = np.random.rand(Ymax+1)
    for i in range (0,Xmax-1):
        for j in range (0,Ymax-1):
            if random_numbers[j]>0.5:
                img[j,i] = [i%255, j%255, 0]
            else:
                img[j,i] = [0,  0,  0]
    return img

for i in range (0,2000):
    x=(x+1)%1000;  y=(y+1)%600
    #time.sleep(10/1000)            
    #cv2.rectangle(img,(0,0),(Xmax,Ymax),(100,0,0),-1)
    #cv2.circle(img,(x,y), radius=10, color=(143,14,143),thickness=2, lineType=cv2.LINE_AA)
    img = rand_binary(img)
    
    
    cv2.imshow('CV_Tutorial', img)
    
    
    key = cv2.waitKey(1)
    if key & 0xFF == 27:
        break
    if key == 112:          # ASCII 112 = 'p'  https://www.asciitable.com/
        key = 0 
        while  not( key == 112): 
            key = cv2.waitKey(1)
cv2.destroyAllWindows()


