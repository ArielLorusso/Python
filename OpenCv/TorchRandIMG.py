import torch
import cv2 
import time

# Define the size of the image
height = 720
width = 1080

def show_random():
    for i in range (0,100):
        # Generate random values for each pixel in the image
        image = torch.rand((height, width, 3))

        # Show the image
        cv2.imshow('image', image.numpy())
        cv2.waitKey(1)


def timer(function):
    start_time = time.perf_counter()
    function()
    end_time = time.perf_counter()
    elapsed_time = end_time - start_time
    return elapsed_time
    
def iterator():
    x=1
    for i in range(1,201):
        x+=x    # x = 2^i
        if not (i%10):
            print(x)  
    print("x:", type(x) ) # x: <class 'int'>
    print(float(x))

elapsed_time = timer(iterator)
print("show_random time: {:.5f} seconds".format(elapsed_time))