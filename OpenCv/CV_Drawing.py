# https://www.youtube.com/watch?v=PtvN8ad9N3g
import numpy as np
import torch
import cv2


image_height = 720 #480
image_width = 1080 #640
center = [550,300]
scroll = 50

img = np.zeros((image_height, image_width, 3), np.uint8)

def check_location(center):
    if center[1] >= image_height:
        center[1] = image_height
    elif center[1] <= 0:
        center[1] = 0
    return center

def draw(layer, center):
    #cv2.rectangle(layer, (center[0],center[1]), (image_width, image_height), (0,0,0), thickness=2, lineType=cv2.LINE_AA)
    cv2.circle(layer, tuple(center), 65, (143,14,143), thickness=2, lineType=cv2.LINE_AA)
    cv2.circle(layer, tuple(center), 70,(255,255,255), thickness=2, lineType=cv2.LINE_AA)
    cv2.circle(layer, tuple(center), 10, (143,14,143), thickness=-1, lineType=cv2.LINE_AA)
    cv2.circle(layer, tuple(center), 5, (255,255,255), thickness=-1, lineType=cv2.LINE_AA)
    return layer

def process_mouse_event(event,x,y,flags, cntr):
    clone = np.zeros((image_height, image_width, 3), np.uint8)
    cv2.line(clone, (5,50), (250,50), (255,255,255), thickness=2, lineType=cv2.LINE_AA)
    cv2.putText(clone, "Scroll ", (10,32), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,255), 2, cv2.LINE_AA)
    if event == cv2.EVENT_MOUSEWHEEL:
        if flags > 0:
            cv2.putText(clone, "Scroll Up", (10,32), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,255), 2, cv2.LINE_AA)
            center[1]-=scroll       
        else:
            center[1]+=scroll
            cv2.putText(clone, "Scroll Down", (10,32), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,255), 2, cv2.LINE_AA)
    _center = check_location(cntr)
    cv2.line(clone, (250,50), tuple(_center), (255,255,255), thickness=2, lineType=cv2.LINE_AA)
    cv2.line(clone, (5,cntr[1]), (image_width-5,cntr[1]), (255,255,255), thickness=2, lineType=cv2.LINE_AA)
    clone = draw(clone, _center)
    cv2.putText(clone, "Center: " + str(_center), (10,80), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (255,255,255), 1, lineType=cv2.LINE_AA)
    cv2.imshow('CV_Scroll_Wheel_Tutorial', clone) 

cv2.imshow('CV_Scroll_Wheel_Tutorial', img)
cv2.setMouseCallback('CV_Scroll_Wheel_Tutorial', process_mouse_event, param=center)
cv2.waitKey(0)
cv2.destroyAllWindows()
