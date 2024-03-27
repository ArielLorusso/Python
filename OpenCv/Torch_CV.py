import numpy as np  # pip install numpy  
import cv2          # pip install opencv-python https://pypi.org/project/opencv-python/

import torch        # https://pytorch.org/get-started/locally/  pip3 install torch torchvision torchaudio
print(torch.__version__)   # 2.0.0+cu117

Ymax = 720; Xmax = 1080

# Create a tensor to hold the image data
img = torch.zeros((Ymax, Xmax, 3), dtype=torch.float32)

# Create a meshgrid of x and y coordinates using torch
y, x = torch.meshgrid(torch.arange(Ymax), torch.arange(Xmax))

# Create a tensor for the R, G, and B channels using x and y coordinates
r = x % 255
g = y % 255
b = torch.zeros((Ymax, Xmax), dtype=torch.float32)

# Concatenate the R, G, and B channels to form the final image tensor
img = torch.stack([r, g, b], dim=-1)

# Convert the tensor to a numpy array and display the image
img = img.numpy().astype(np.uint8)
for i in range (0,100):
    if i % 2:
        b = torch.ones((Ymax, Xmax), dtype=torch.float32)*200
    else:
        b = torch.zeros((Ymax, Xmax), dtype=torch.float32)

    img = torch.stack([r, g, b], dim=-1)
    img = img.numpy().astype(np.uint8)
    cv2.imshow('image', img)
    cv2.waitKey(1)