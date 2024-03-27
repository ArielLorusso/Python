from skimage.filters.rank import entropy # https://scikit-image.org/docs/stable/api/skimage.filters.rank.html
from skimage.morphology import disk      # https://scikit-image.org/docs/stable/api/skimage.morphology.html#skimage.morphology.disk

from skimage import io
import matplotlib.pyplot as plt
import numpy as np

################### ENTROPY

path = "/home/ariel/Desktop/scratch.png"  #  download.jpg  photo.webp
img = io.imread(path, as_gray=True)
entropy_img = entropy(img, disk(5))

from skimage.filters import threshold_otsu , threshold_yen
thresh = threshold_otsu(entropy_img)
binary = entropy_img <= thresh
#plt.imshow(1-binary); plt.show()


################### AUTOMATED  (FOLDER MUST ONLY CONTAIN IMAGES)
import os
import glob

time_list = []; area_list = []
time = 0

path = "/home/ariel/Desktop/IMAGES/scratch/*"     # *: any file inside folder 
path =  sorted( glob.glob(path), key=os.path.getmtime ) #https://docs.python.org/3/library/os.path.html#os.path.getatime

for file in path:
    img = io.imread(file, as_gray=True)
    entropy_img = entropy(img, disk(10))
    thresh= threshold_yen(entropy_img)
    binary = entropy_img <= thresh - 0.3
#    plt.subplot(2,1,1); plt.imshow(binary)
#    plt.subplot(2,1,2); plt.imshow(img); plt.show()
    area = np.sum(binary==1)/(np.sum(binary==0)+np.sum(binary==1))
    print ( area , time)
    time_list.append(time)
    area_list.append(area)
    time += 1

plt.plot( time_list,area_list,'bo'); plt.show()
from scipy.stats import linregress
#slope, intercept ,r_value, p_value, std_err = linregress()
print(linregress(time_list,area_list))
slope,intercept,rvalue,pvalue,stderr = linregress(time_list,area_list)
print ("R\N{SUPERSCRIPT TWO} =",rvalue**2 )

# bash commands for batch compression ffmpeg compresses double
# for i in *.png ; do convert "$i" "${i%.*}.jpg" ; done
# for i in *.png;  do ffmpeg -i "$i" "${i%.*}.jpg"; done
