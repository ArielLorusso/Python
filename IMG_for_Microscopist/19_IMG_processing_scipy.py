path = "/home/ariel/Desktop/download.jpg"

# from scipy import misc # https://docs.scipy.org/doc/scipy/tutorial/index.html#user-guide
# scipy.misc is deprecated and has no attribute imread.
# https://docs.scipy.org/doc/scipy-1.1.0/reference/misc.html  <-- OLD DOCUMENTATION
"""
import imageio      #  https://imageio.readthedocs.io/en/stable/
img = imageio.imread(path)
print(type(img))
"""
                        # https://scikit-image.org/docs/stable/
from skimage    import io, img_as_ubyte  # pip install (numpy,scikit-image)
from matplotlib import pyplot as plt  #https://matplotlib.org/stable/plot_types/index.html


img = io.imread(path);     print(img.shape, img.dtype)  # (157, 321, 3) uint8 Tensor similar to Torch dim=3
plt.subplot(2,2,1); io.imshow(img)
img2 = io.imread(path, as_gray=True);   print(img.dtype)  # float64
img2 = img_as_ubyte(img2);   print(img2.shape, img2.dtype)  # (157, 321) uint8
plt.subplot(2,2,2); io.imshow(img2,cmap="flag");  plt.show()

'''print(img[10:15,20:25]) 
mean = img.mean() # 0
max  = img.max()  # 255
min  = img.min()  # 107.68
print(min,max,mean)'''

import numpy    as     np
# FLIP & TONEMAP   https://matplotlib.org/stable/tutorials/colors/colormaps.html
flipped = np.fliplr(img2)
plt.subplot(2,2,3);  io.imshow(flipped, cmap="cubehelix") # natural
flipped2 = np.flipud(img2)
plt.subplot(2,2,4);  io.imshow(flipped2, cmap= "rainbow" ) # temperature
plt.show()

io.imshow(flipped, cmap="hsv") # "gnuplot2" "magma" "CMRmap" "rainbow" "jet"
plt.show() # "hsv" "Greys"    "virdis":defaultgreen


from scipy      import ndimage

rotate = ndimage.rotate(img, 45, reshape=False)
img2 = img_as_ubyte(io.imread(path,as_gray=True))  
uniform_filter  = ndimage.uniform_filter (img, size=4)
gaussian_filter = ndimage.gaussian_filter(img, sigma=4)
median_filter   = ndimage.median_filter  (img, 4)
sobel_filter    = ndimage.sobel          (img2,axis=0)
plt.imshow(sobel_filter,"rainbow");plt.show()
