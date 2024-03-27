# pip install scikit-image==0.18.3
# https://www.youtube.com/watch?v=6P8YhJa2V6o&list=PLZsOBAyNTZwYx-7GylDo3LSYpSompzsqW&index=9

# https://stackoverflow.com/questions/56763416/what-is-diffrence-between-number-and-repeat-in-python-timeit
"""         samples = []
            for _ in range(repeat):
                # start timer
                for _ in range(number):
                    do_work()
                # end timer
                samples.append(duration)
            """

import timeit
import statistics

loops = 10
############################################################
################  MEDIAN                           66 ± .7 ms
# Provide the necessary setup code
median_filter_code = "median_img  =  nd.median_filter(img, size=3)"
median_setup_code = """
from scipy import ndimage as nd
from skimage import img_as_float, io
img = img_as_float(io.imread("images/night_noise.jpg"))
"""
times = timeit.repeat(median_filter_code, repeat=loops, number=1, setup=median_setup_code)
time_taken = min(times)
stdev_time = statistics.stdev(times)
total_time = sum(times)
print("best "f"{time_taken * 1e6:.1f} μs ± {stdev_time * 1e6:.1f} μs "
       +" total of "f"{total_time} in "f"{loops} loops for median filter")
############################################################
################  GAUSSIAN                         12 ± .6 ms
# Provide the necessary setup code
gaussian_filter_code = "gaussian_img  =  nd.gaussian_filter(img, sigma=3)"
gaussian_setup_code = """
from scipy import ndimage as nd
from skimage import img_as_float, io
img = img_as_float(io.imread("images/night_noise.jpg"))
"""
times = timeit.repeat(gaussian_filter_code, repeat=loops, number=1, setup=gaussian_setup_code)
time_taken = min(times)
stdev_time = statistics.stdev(times)
total_time = sum(times)
print("best "f"{time_taken * 1e6:.1f} μs ± {stdev_time * 1e6:.1f} μs "
       +"total of "f"{total_time} in "f"{loops} loops for gaussian filter")
############################################################
################  RANDOM WALK                   82 ± 1 ms
# Provide the necessary setup code
random_filter_code = """
denoise_img = denoise_nl_means(img, h=1.15 * sigma_est, fast_mode=True, **patch_kw)
"""
random_setup_code = """
from skimage.restoration import denoise_nl_means, estimate_sigma
from skimage import img_as_float, io
import numpy as np 
img = img_as_float(io.imread("images/night_noise.jpg"))
sigma_est = np.mean(estimate_sigma(img, multichannel=True))
patch_kw = dict(patch_size=5,   patch_distance=6,     multichannel=True)
"""
times = timeit.repeat(random_filter_code, repeat=loops, number=1, setup=random_setup_code)
time_taken = min(times)
stdev_time = statistics.stdev(times)
total_time = sum(times)
print("best "f"{time_taken * 1e6:.1f} μs ± {stdev_time * 1e6:.1f} μs "
       +"total of "f"{total_time} in "f"{loops} loops for random_walk filter")
############################################################
############################################################
################  CV2 MEDIAN                   1.5 ± 0.1 ms
# Provide the necessary setup code
CV_median_filter_code = """
median      = cv2.medianBlur(img,5)
"""
CV_median_setup_code = """
import cv2  
img  = cv2.imread("images/night_noise.jpg")
"""
times = timeit.repeat(CV_median_filter_code, repeat=loops, number=1, setup=CV_median_setup_code)
time_taken = min(times)
stdev_time = statistics.stdev(times)
total_time = sum(times)
print("best "f"{time_taken * 1e6:.1f} μs ± {stdev_time * 1e6:.1f} μs "
      +" total of "f"{total_time} in "f"{loops}loops for CV_median filter")
############################################################
################  CV2 GAUSSIAN                   1.5 ± 0.1 ms
import matplotlib.pyplot as plt
loops = 20
# Provide the necessary setup code
CV_gaussian_filter_code = """
gauss_blur  = cv2.GaussianBlur(img, (5,5), 0)
"""
CV_gaussian_setup_code = """
import cv2
import numpy as np
img  = cv2.imread("images/night_noise.jpg")
"""
times = timeit.repeat(CV_gaussian_filter_code, repeat=loops, number=1, setup=CV_gaussian_setup_code)
time_taken = min(times)
stdev_time = statistics.stdev(times)
total_time = sum(times)
print("best "f"{time_taken * 1e6:.1f} μs ± {stdev_time * 1e6:.1f} μs "+
      "total of "f"{total_time} in "f"{loops} loops for CV_gaussian filter")
############################################################
################  CV2 GRAY GAUSSIAN                   1.5 ± 0.1 ms
import matplotlib.pyplot as plt
loops = 20
# Provide the necessary setup code
CV_gaussian_filter_code = """
gauss_blur  = cv2.GaussianBlur(img, (5,5), 0)
"""
CV_gaussian_setup_code = """
import cv2
import numpy as np
img  = cv2.imread("images/night_noise.jpg", cv2.IMREAD_GRAYSCALE)
"""
# Measure the time
times = timeit.repeat(CV_gaussian_filter_code, repeat=loops, number=1, setup=CV_gaussian_setup_code)
# Calculate statistics
time_taken = min(times)
stdev_time = statistics.stdev(times)
total_time = sum(times)
# Print summary
print("best "f"{time_taken * 1e6:.1f} μs ± {stdev_time * 1e6:.1f} μs "+
      "total of "f"{total_time} in "f"{loops} loops for CV_BW_gaussian filter")





