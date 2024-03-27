
from skimage import io
from matplotlib import pyplot as plt

path = "/home/ariel/Desktop/download.jpg"
img = io.imread(path, as_gray=True)

from skimage.transform import rescale,resize,downscale_local_mean
rescaled_img   = rescale(img, 1.1/4, anti_aliasing=True)
downscaled_img = downscale_local_mean(img,(4,4) )#vertical,horizontal=(4,3)
#plt.subplot(2,1,1);io.imshow(rescaled_img,cmap="cubehelix")
#plt.subplot(2,1,2);io.imshow(downscaled_img,cmap="cubehelix"); # similar but more detail
#plt.show()

from skimage.filters import roberts, sobel, scharr ,prewitt
edge_roberts = roberts(img)
edge_sobel   = sobel(img)  
edge_scharr  = scharr(img)
edge_prewitt = prewitt(img)
fig, axes = plt.subplots(nrows=2,ncols=2 , figsize=(8,8)); ax = axes.ravel()
ax[0].imshow(edge_roberts)  ; ax[0].set_title("roberts")
ax[1].imshow(edge_scharr)   ; ax[1].set_title("schar")
ax[2].imshow(edge_sobel)    ; ax[2].set_title("sobel")
ax[3].imshow(edge_prewitt)  ; ax[3].set_title("prewit")
for a in ax: a.axis('off')
plt.show()

from skimage.feature import canny
edge_canny = canny(img, sigma=2)
plt.subplot(1,1,1); io.imshow(edge_canny); plt.show()


img = io.imread(path, as_gray=True)

import numpy as np
import scipy.stats as st
def gkern (kernel=21,nsig=2):       # 2D GAUSIAN KERNELL
    lim = kernel//2 + (kernel%2)/2     # lim is sqrt(kernell)+.5 = 5
    x = np.linspace(-lim,lim,kernel+1)
    kern1d = np.diff(st.norm.cdf(x))
    kern2d = np.outer(kern1d,kern1d)
    return kern2d/kern2d.sum()

from skimage import restoration
psf_1 = np.ones((3,3))/9 # Point_Spread_Function matrix
psf_2 = gkern(5,3)       # Point_Spread_Function matrix

deconvolved_1,_ = restoration.unsupervised_wiener(img,psf_1)
deconvolved_2,_ = restoration.unsupervised_wiener(img,psf_2)
plt.subplot(2,1,1); io.imshow(img,cmap="jet") 
plt.subplot(2,1,2); io.imshow(deconvolved_2,cmap="jet"); plt.show()



#name = path.split(".")
#plt.imsave(name[0]+"_deconv.jpg",deconvolved, cmap="cubehelix")

path = "/home/ariel/Desktop/photo.webp"  #  download.jpg  photo.webp
from matplotlib import pyplot as plt
from skimage import io, restoration      # https://scikit-image.org/docs/stable/auto_examples/
from skimage.filters.rank import entropy # https://scikit-image.org/docs/stable/api/skimage.filters.rank.html
from skimage.morphology import disk      # https://scikit-image.org/docs/stable/api/skimage.morphology.html#skimage.morphology.disk
img = io.imread(path, as_gray=True)
entropy_img = entropy(img, disk(4))
#io.imshow( entropy_img ); plt.show()
#io.imshow( img ); plt.show()

from skimage.filters import try_all_threshold
#fig, ax = try_all_threshold(entropy_img, figsize=(10,10), verbose=False)
#plt.show()

import numpy as np
from skimage.filters import threshold_yen
thresh = threshold_yen(entropy_img)
binary = entropy_img <= thresh
io.imshow( binary ); plt.show()

print(" the '%' of brigt pix =",(np.sum(binary==1)*100)/((np.sum(binary==1))+(np.sum(binary==0))))
print(" those are low entropy")