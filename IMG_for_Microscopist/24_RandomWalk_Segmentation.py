# pip install scikit-image==0.18.3
# https://www.youtube.com/watch?v=6P8YhJa2V6o&list=PLZsOBAyNTZwYx-7GylDo3LSYpSompzsqW&index=9


from skimage import io, img_as_float 
import matplotlib.pyplot as plt
import numpy as np 
from skimage.restoration import denoise_nl_means, estimate_sigma


import cv2
import numpy as np

img = img_as_float(io.imread("images/Alloy_noisy.jpg"))

# sigma_est = np.mean(estimate_sigma(img, multichannel=True))
# plt.figure(0 ,label="HISTOGRAM")  # HISTOGRAM
# plt.subplot(2,2,1); plt.hist(img.flat ,bins=100,range=(0,1))
# plt.subplot(2,2,2); plt.imshow(img)
# from scipy import ndimage as nd
img        = cv2.imread("images/Alloy_noisy.jpg")
gauss_img  = cv2.medianBlur(img,3)
# plt.subplot(2,2,3); plt.hist(gauss_img.flat ,bins=100,range=(0,1))
# plt.subplot(2,2,4); plt.imshow(gauss_img);plt.show()

# img = img_as_float(io.imread("images/Alloy_noisy.jpg"))
# patch_kw = dict(patch_size=5,       # 5x5 patches
#                 patch_distance=6,   # 13x13 search area
#                 multichannel=True)

# #slow algorithm
# denoise_img = denoise_nl_means(img, h=1.15 * sigma_est, fast_mode=True, **patch_kw)
# plt.subplot(1,2,1); plt.imshow(gauss_img)
# plt.subplot(1,2,2); plt.imshow(denoise_img);plt.show()

# from skimage import exposure 
# # eq_denois_img = exposure.equalize_adapthist(denoise_img)
# eq_gauss_img = exposure.equalize_adapthist(gauss_img)

# plt.figure(1 ,label=" CLEAN EQ")  # 1
# plt.subplot(2,2,1); plt.imshow(eq_denois_img)
# plt.subplot(2,2,2); plt.hist(eq_denois_img.flat ,bins=100,range=(0,1))
# plt.subplot(2,2,3); plt.imshow(eq_gauss_img)
# plt.subplot(2,2,4); plt.hist(eq_gauss_img.flat ,bins=100,range=(0,1))
# plt.show()

import numpy as np
import matplotlib.pyplot as plt
from skimage import io, img_as_float
from skimage import exposure
from skimage.segmentation import random_walker

# Load and preprocess the image
img = img_as_float(io.imread("images/night_noisy.jpg"))
eq_gauss_img = exposure.equalize_adapthist(img, clip_limit=0.03)
# Display the histogram
plt.hist(eq_gauss_img.flat, bins=100, range=(0, 1))
plt.show()
# Create markers for random walker
markers = np.zeros(img.shape, dtype=np.uint)
markers[(eq_gauss_img < 0.6)  & (eq_gauss_img > 0.3)] = 1
markers[(eq_gauss_img < 0.99) & (eq_gauss_img > 0.8)] = 2
# Apply random walker segmentation
labels = random_walker(eq_gauss_img, markers, beta=10, mode='bf')
# Create segments based on labels
segm1 = (labels == 1)
segm2 = (labels == 2)
# Create an RGB array for visualization
all_segments = np.zeros_like(img)
# Assign colors using boolean indexing for each channel
all_segments[..., 0][segm1] = 1  # Red channel
all_segments[..., 1][segm2] = 1  # Green channel
# Display the segmented image
plt.imshow(all_segments)
plt.show()
