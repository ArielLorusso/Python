import cv2

# LOAD
file_dir = "images/balloons_noisy.png"
#file_dir = "images/people.jpg"
#file_dir = "images/Low.jpg"
img_original  = cv2.imread(file_dir)
img_grayscale = cv2.imread(file_dir,0)

# SHOW WINDOW 
def test_1 ():
    cv2.namedWindow('WINDOW OG  ', cv2.WINDOW_GUI_NORMAL)    # CUSTOM window    
        # cv2.cv2.WINDOW_GUI_NORMAL     – NO GUI buttons      _GUI_EXPANDED (default buttons)
        # cv2.WINDOW_AUTOSIZE(Default)  – fixed  window size  _NORMAL  (variable sizw)
        # cv2.WINDOW_FULLSCREEN         – Changes the window size to fullscreen
        # cv2.WINDOW_KEEPRATIO          - resize keep ratio  _FREERATIO (distorts image)
    cv2.resizeWindow('WINDOW OG  ', 600, 300)                 # RESIZE  X=600,Y=300
    cv2.imshow("WINDOW OG  ", img_original);    # COLOR
    cv2.imshow("WINDOW GRAY", img_grayscale);   # GRAY
    cv2.waitKey(0);  cv2.destroyAllWindows()
# test_1()

# COLOR MODE / SEGMENTATION                                          https://learnopencv.com/color-spaces-in-opencv-cpp-python/
def test_2 ():                                                     # FULL   cvtColor()   LIST :
    img_LAB = cv2.cvtColor(img_original, cv2.COLOR_BGR2LAB  )      # https://docs.opencv.org/3.4/d8/d01/group__imgproc__color__conversions.html
    img_YCB = cv2.cvtColor(img_original, cv2.COLOR_BGR2YCrCb)
    img_HSV = cv2.cvtColor(img_original, cv2.COLOR_BGR2HSV  )
    cv2.imshow("WINDOW LAB ", img_LAB);   # LAB =  L – Lightness   A – color Green ~ Magenta. B – color Blue ~ Yellow.
    cv2.imshow("WINDOW YCB ", img_YCB);   # YCB
    cv2.imshow("WINDOW HSV ", img_HSV);   # HSV     Hue ( H ), Saturation ( S ) and Value ( V ) 
    cv2.waitKey(0);  cv2.destroyAllWindows()
#test_2()

# 4   BIT  GRAY  SAVE
def test_3 ():                                                         # Step 1: Load alredy done : img_original 
    img_gray = cv2.cvtColor(img_original, cv2.COLOR_BGR2GRAY)          # Step 2: Convert  image     to   grayscale
    img_4bit = cv2.normalize(img_gray, None, 0, 15, cv2.NORM_MINMAX)   # Step 3: Convert  grayscale to   4-bit
    cv2.imshow("4-bit Grayscale Image", img_4bit)                      # Step 4: Display  4-bit                
    cv2.waitKey(0);  cv2.destroyAllWindows()
    output_file_dir  = "images/balloons_4bit_grayscale.jpg"            # Step 5: Save   4-bit   image         
    cv2.imwrite(output_file_dir,  img_4bit)
    import matplotlib.pyplot  as plt
    plt.imshow(img_4bit, cmap='hot'); plt.show()       # CHANGES THE IMAGE ! (make copy or use at the end )
#test_3()

# 555 BIT GRAY                  cv2.COLOR_GRAY2BGR  ???
def test_3_2 ():                                                # Step 1: Load alredy done : img_original 
                                                                # Step 2: Convert the image to 5-bit color representation
    img_5bit = (img_original // 8)                               #   Reduces each channel to 5 bits
    #  	Floor division : //   truncate each channel to nearest lower multiple of 8   
    #   8bit/5bit = 2^8/2^5 = 8 (skip values )..... 0,8,16,32,40,48,56,72,80...256  =  (img_original // 8)  * 8
    cv2.imshow("5-bit Color Image", img_5bit)                   # Step 3: Display the 5-bit color image
    cv2.waitKey(0);  cv2.destroyAllWindows()
    output_file_dir2 = "images/balloons_5bit_color1.jpg"         # Step 4: Save the 5-bit color image
    cv2.imwrite(output_file_dir2, img_5bit)
#test_3_2()

# 555 BIT COLOR                 cv2.CV_16U ???
def test_3_3 ():                                                # Step 1: Load alredy done : img_original 
                                                                # Step 2: Convert the image to 5-bit color representation
    img_5bit = (img_original // 8)                                          #   Reduces each channel to 5 bits
    #  	Floor division : //   truncate each channel to nearest lower multiple of 8   
    #   8bit/5bit = 2^8/2^5 = 8 (skip values )..... 0,8,16,32,40,48,56,72,80...256     
    import numpy as np

    bgr555 = np.zeros_like(img_5bit[:, :, 0], dtype=np.uint16)   # Step 3: Convert the 5-bit color image to BGR555 manually
    bgr555 |= ((img_5bit[:, :, 2] ) >> 10).astype(np.uint16)            # Red channel
    bgr555 |= ((img_5bit[:, :, 1] ) >> 5 ).astype(np.uint16)            # Green channel
    bgr555 |= ((img_5bit[:, :, 0] ) >> 0 ).astype(np.uint16)            # Blue channel
    cv2.imshow("5-bit Color Image", bgr555)                     # Step 4: Display the 5-bit color image
    cv2.waitKey(0);   cv2.destroyAllWindows()
    import matplotlib.pyplot  as plt
    plt.imshow(img_5bit, cmap='hot'); plt.show()                        # CHANGES THE IMAGE ! (make copy or use at the end )

    output_file_dir2 = "images/balloons_5bit_color2.jpg"         # Step 5: Save the 5-bit color image
    cv2.imwrite(output_file_dir2, bgr555.astype(np.uint8))              # Convert back to 8-bit for saving
#test_3_3()

# CROP RORATE RESIZE            #  https://learnopencv.com/image-rotation-and-translation-using-opencv/
def test_4 ():          
    height, width = img_original.shape[:2]                # get the center coordinates of the image to create the 2D rotation matrix
    center = (width/2, height/2)                          # using cv2.getRotationMatrix2D() to get the rotation matrix
    rotate_matrix = cv2.getRotationMatrix2D(center=center, angle=45, scale=1)
    rotated_image = cv2.warpAffine(src=img_original, M=rotate_matrix, dsize=(width, height))
    
    cv2.imshow("ROTATED", rotated_image );  cv2.waitKey(0)
    crop_img = cv2.resize(img_original, (200,200), interpolation = cv2.INTER_CUBIC)
    cv2.imshow("RESIZE", crop_img);  cv2.waitKey(0)
    crop_img = img_original[0:30, 0:100].copy()     # CROP from Top Left y:y_f , x:x_f
    crop_img = cv2.resize(crop_img, (1200,200), interpolation = cv2.INTER_CUBIC)
    cv2.imshow("CROPPED", crop_img);  cv2.waitKey(0)
    
    import numpy as np
    tx, ty = width / 4, height / 4  # get tx and ty TRANSLATION values for translation
    translation_matrix = np.array([ [1, 0, tx],     # create the translation matrix using tx and ty, it is a NumPy array 
                                    [0, 1, ty]  ], dtype = np.float32)
    transl_image = cv2.warpAffine(src=img_original, M=translation_matrix, dsize=(width, height))
    cv2.imshow("CROPPED", transl_image);  cv2.waitKey(0);    cv2.destroyAllWindows()
#test_4()

# DETAIL ENTROPY
def test_5 ():
    from skimage import io # restoratiom
    from skimage.filters.rank import entropy
    from skimage.morphology import disk
    import pandas as pd
    import matplotlib.pyplot as plt


    #img_gray = cv2.cvtColor(img_original, cv2.COLOR_BGR2GRAY)
    img_gray = io.imread('images/people.jpg', as_gray=True)
    
    entropy_img  = entropy(img_gray, disk(1))
    entropy_img2 = entropy(img_gray, disk(3))
    entropy_img3 = entropy(img_gray, disk(10))

    cv2.imshow('gray', img_gray)
    cv2.imshow('entropy1' , entropy_img)
    cv2.imshow('entropy3' , entropy_img2)
    cv2.imshow('entropy10', entropy_img3)
    cv2.waitKey(0);    cv2.destroyAllWindows()
    # plt.imshow( img_gray, cmap='hot')
    # plt.show()      
    # plt.imshow( entropy_img, cmap='hot')    
    # plt.show()
# test_5()

# DETAIL MORPHOLOGY
def test_5_2 ():
    import numpy as np
    img_gray = cv2.cvtColor(img_original, cv2.COLOR_BGR2GRAY)
    kernel = np.ones((3, 3), np.uint8)
    gradient = cv2.morphologyEx(img_gray, cv2.MORPH_GRADIENT, kernel) * 3 % 255
    cv2.imshow('Morphological Gradient', gradient)
    cv2.waitKey(0);    cv2.destroyAllWindows()
# test_5_2 ()
 
# DETAIL LAPLACIAN      https://theailearner.com/tag/cv2-laplacian/
def test_5_3 ():
    img_gray = cv2.cvtColor(img_original, cv2.COLOR_BGR2GRAY)
    laplacian = cv2.Laplacian(img_gray, cv2.CV_64F)
    cv2.imshow('Laplacian Filter', laplacian)
    cv2.waitKey(0);  cv2.destroyAllWindows()
# test_5_3 ()

###############################################################################
# HISTOGRAM Min-Max Stretching
# HISTOGRAM Projection              https://theailearner.com/2019/04/18/histogram-backprojection/

# HISTOGRAM CLAHE
def test_5 ():  pass

# DENOISE Blur
def test_6 ():  
    from skimage import restoration
    from scipy.signal import convolve2d
    import numpy as np
    #from scipy import ndimage as nd
    #img_gauss  = nd.gaussian_filter(img_original, sigma=2)
    #img_gauss2 = nd.uniform_filter(img_original, size=(2, 2, 1))
    img_blur    = cv2.blur(img_original, (2, 2) )
    img_median  = cv2.medianBlur(img_original,3)  # size  3 ~ 9  
    img_median2 = cv2.medianBlur(img_original,5)
    #img_median2 = cv2.bilateralFilter(img_original,5)
    
    psf = np.ones((5, 5)) / 25
    rest = restoration.wiener(cv2.cvtColor(img_original,cv2.COLOR_BGR2GRAY),psf,1100)
    #img_gauss3 = cv2.GaussianBlur(img_original,(3,3),cv2.BORDER_DEFAULT)  # size  3 ~ 9

    cv2.imshow("img_OG",img_original);      
#    cv2.imshow("img_gauss",img_gauss);      
#    cv2.imshow("img_gauss2",img_gauss2);    
    cv2.imshow("img_blur",img_blur)
    cv2.imshow("img_median",img_median)
    cv2.imshow("img_median2",img_median2)
    cv2.imshow("REST",rest)
    cv2.waitKey(0);  cv2.destroyAllWindows()
#test_6()

# MORPHOLOGICAl DILATATION      https://medium.com/@mmas/python-image-processing-libraries-performance-opencv-vs-scipy-vs-scikit-image-65e4b79b2e7e

# TRESHOLD
def test_7 ():  pass

# OTSU
def test_8 ():  pass

# FOURIER
def test_9 ():
    import numpy as np

    img = cv2.imread('images/BSE.jpg', 0) # load an image

    
    dft = cv2.dft(np.float32(img), flags=cv2.DFT_COMPLEX_OUTPUT)    # Output is a 2D complex array. 1st Real , 2nd Imaginary
                 #  cv2.fft  input image :  float32

    dft_shift = np.fft.fftshift(dft)    # Center  Fourier transform X 
    # by shifting the zero-frequency  component to the center of the array.
    # Otherwise it starts at the tope left corenr of the image (array)

    magnitude_spectrum = 20 * np.log(cv2.magnitude(dft_shift[:, :, 0], dft_shift[:, :, 1]))     # Magnitude of the function is 20.log(abs(f))
    # For values that are 0 we may end up with indeterminate values for log.  So we can add 1 to the array to avoid seeing a warning. 

    # Circular HPF mask, center circle is 0, remaining all ones
    #Can be used for edge detection because low frequencies at center are blocked
    #and only high frequencies are allowed. Edges are high frequency components.
    #Amplifies noise.
    rows, cols = img.shape
    crow, ccol = int(rows / 2), int(cols / 2)

    mask = np.ones((rows, cols, 2), np.uint8)
    r = 80
    center = [crow, ccol]
    x, y = np.ogrid[:rows, :cols]
    mask_area = (x - center[0]) ** 2 + (y - center[1]) ** 2 <= r*r
    mask[mask_area] = 0
    fshift = dft_shift * mask

    fshift_mask_mag = 2000 * np.log(cv2.magnitude(fshift[:, :, 0], fshift[:, :, 1]))
    f_ishift = np.fft.ifftshift(fshift)
    img_back = cv2.idft(f_ishift)
    img_back = cv2.magnitude(img_back[:, :, 0], img_back[:, :, 1])


# SOBEL
def test_10 ():  pass

# CANNY EDGE
def test_11 ():  pass

# SUPER RESOLUTION    (USE  "FSRCNN_x2" Twice  )   EDSR ESPCN FSRCNN LapSRN  https://learnopencv.com/super-resolution-in-opencv   
def test_12_1 ():
    import numpy as np
    img_low = cv2.imread("images/Low.png")

    folder = '/home/ariel/Pictures/'

    sr = cv2.dnn_superres.DnnSuperResImpl_create()                                      
    #file12 = "EDSR_x2.pb"        # x 2,3,4   https://github.com/Saafke/EDSR_Tensorflow/    #           x2       x4  
    #file14 = "EDSR_x4.pb"        # x 2,3,4                                                 WOOW   9600 ms    10 seg  36.8 MB     x4 Best result (SLOW AS FuK )           
    file22 = "ESPCN_x2.pb"        # x 2,3,4   https://github.com/fannymonori/TF-ESPCN/       Wow     13 ms     18 ms   90 KB       (GOOD x4   Best for PERFORMANCE )            
    file24 = "ESPCN_x4.pb"        # x 2,3,4        
    file32 = "FSRCNN_x2.pb"       # x 2,3,4   https://github.com/Saafke/FSRCNN_Tensorflow    Wow     26 ms     28 ms   40 KB       x2 WINNER     (Bad x4)
    file34 = "FSRCNN_x4.pb"       
    #file342 = "FSRCNN-small_x4.pb"# x 2,3,4   https://github.com/Saafke/FSRCNN_Tensorflow   Hmm                       10 KB                     (Bad x4)       (Bad x2)
    file42 = "LapSRN_x2.pb"       # x 2,4,8   https://github.com/fannymonori/TF-LapSRN/      wow    120 ms    705 ms  2.6 MB      x4 WINER after cv2.blur(2,2) (Bad x2)(Bad x8)
    file44 = "LapSRN_x4.pb"       # x 2,4,8   
    #file48 = "LapSRN_x8.pb"      # x 2,4,8    https://github.com/fannymonori/TF-LapSRN/     Hmm    3500 ms           3.2 MB      MALO peor que x4 
    #sr.readModel( folder + file14 );  sr.setModel("edsr", 4); result11 = sr.upsample(img_low)   
    #sr.readModel( folder + file32 );  sr.setModel("edsr", 2); result12 = sr.upsample(result32)    # WORST  ( Same as Best but 10000x SLOW )
    sr.readModel( folder + file24 ); sr.setModel("espcn", 4); result21 = sr.upsample(img_low)      # 1) (BEST perf) Conects light tones
    sr.readModel( folder + file22 ); sr.setModel("espcn", 2); result22 = sr.upsample(img_low)      # 
    sr.readModel( folder + file22 ); sr.setModel("espcn", 2); result23 = sr.upsample(result22)     # 
    sr.readModel( folder + file34 ); sr.setModel("fsrcnn",4); result31 = sr.upsample(img_low)      # UGLY
    sr.readModel( folder + file32 ); sr.setModel("fsrcnn",2); result32 = sr.upsample(img_low)     
    sr.readModel( folder + file32 ); sr.setModel("fsrcnn",2); result33 = sr.upsample(result32)     # 2) (MORE Truth conservs black tones) 
    sr.readModel( folder + file44 ); sr.setModel("lapsrn",4); result41 = sr.upsample(img_low)      # 3) (if you can wait 30x )
    sr.readModel( folder + file42 ); sr.setModel("lapsrn",2); result42 = sr.upsample(img_low)      
    sr.readModel( folder + file42 ); sr.setModel("lapsrn",2); result43 = sr.upsample(result42)      #  )
#    sr.readModel( folder + file6 ); sr.setModel("lapsrn",8);  result6 = sr.upsample(img_low)
    #Resized image
    #resized = cv2.resize(img_low,dsize=None,fx=2,fy=2)
    #cv2.imshow("SUPER1", result11) 
    result2 =  cv2.blur(result21, (2, 2) )
    cv2.imshow("SUPER 21", result21)    # <- 2/3)
    cv2.imshow("SUPER 31", result31)    #    5  ) Worst x4    
    cv2.imshow("SUPER 41", result41)    # <- 1  ) BEST  x4    LapSRN_x4
    cv2.imshow("SUPER 23", result23)    #    4  )
    cv2.imshow("SUPER 33", result33)    # <- 2/3) BEST  x2x2  FSRCNN_x2  <-
    cv2.imshow("SUPER 43", result43)    #    6  ) WORST x2x2

    cv2.waitKey(0); cv2.destroyAllWindows()
test_12_1()
def test_12_2 ():
    img_low = cv2.imread("images/lara.png")
    folder = '/home/ariel/Pictures/'

    sr = cv2.dnn_superres.DnnSuperResImpl_create()                                      #           x3      
    #file1 = "EDSR_x3.pb"        # x 2,3,4   https://github.com/Saafke/EDSR_Tensorflow/    WOOW   9600 ms     36.8 MB         
    file2 = "ESPCN_x3.pb"       # x 2,3,4   https://github.com/fannymonori/TF-ESPCN/       Wow      13 ms      90 KB          
    #file3 = "FSRCNN_x3.pb"       # x 2,3,4   https://github.com/Saafke/FSRCNN_Tensorflow   Wow     26 ms      40 KB 
    #file4 = "FSRCNN-small_x3.pb"# x 2,3,4   https://github.com/Saafke/FSRCNN_Tensorflow    Hmm     13 ms      10 KB  

  #  sr.readModel( folder + file1 );  sr.setModel("edsr", 3); result1 = sr.upsample(img_low)   
    sr.readModel( folder + file2 );  sr.setModel("espcn",  3); result2 = sr.upsample(img_low)
    #sr.readModel( folder + file3 );   sr.setModel("fsrcnn",3); result3 = sr.upsample(img_low)
    #sr.readModel( folder + file4 );  sr.setModel("fsrcnn", 3); result4 = sr.upsample(img_low)
    #cv2.imshow("SUPER1", result1) 
    result2 =  cv2.blur(result2, (2, 2) )
    #result3 =  cv2.blur(result3, (2, 2) )
    #result4 =  cv2.blur(result4, (2, 2) )
    cv2.imshow("SUPER2", result2)
    #cv2.imshow("SUPER3", result3)    
    #cv2.imshow("SUPER4", result4)
    cv2.waitKey(0);cv2.destroyAllWindows() 
#test_7_2()
def test_12_3 ():
    import timeit
    import statistics

    loops = 4

    # Provide the necessary setup code
    setup_code = """
import cv2
img_low = cv2.imread("images/Low.png")
folder = '/home/ariel/Pictures/'
file1  = "EDSR_x4.pb"
file2  = "ESPCN_x4.pb"
file3  = "FSRCNN_x4.pb"
file4  = "LapSRN_x4.pb" 
file5  = "ESPCN_x3.pb" 
file6  = "FSRCNN_x3.pb" 
sr = cv2.dnn_superres.DnnSuperResImpl_create()
    """

    filter_code1 = """sr.readModel(folder + file1); sr.setModel("edsr"  , 4); result1 = sr.upsample(img_low)"""
    filter_code2 = """sr.readModel(folder + file2); sr.setModel("espcn" , 4); result2 = sr.upsample(img_low)"""
    filter_code3 = """sr.readModel(folder + file3); sr.setModel("fsrcnn", 4); result3 = sr.upsample(img_low)"""
    filter_code4 = """sr.readModel(folder + file4); sr.setModel("lapsrn", 4); result4 = sr.upsample(img_low)"""
    filter_code5 = """sr.readModel(folder + file5); sr.setModel("espcn",  3); result4 = sr.upsample(img_low)"""
    filter_code6 = """sr.readModel(folder + file6); sr.setModel("fsrcnn", 3); result4 = sr.upsample(img_low)"""

    times = timeit.repeat(filter_code1, repeat=loops, number=1, setup=setup_code)
    time_taken = min(times);   stdev_time = statistics.stdev(times);    total_time = sum(times)
    print("Best time for EDSR:  ", f"{time_taken * 1e6:.1f} μs ± {stdev_time * 1e6:.1f} μs total of "f"{total_time}  in "f"{loops} loops")

    times = timeit.repeat(filter_code2, repeat=loops, number=1, setup=setup_code)
    time_taken = min(times);   stdev_time = statistics.stdev(times);    total_time = sum(times)
    print("Best time for ESPCN: ", f"{time_taken * 1e6:.1f} μs ± \t{stdev_time * 1e6:.1f} μs total of "f"{total_time}  in "f"{loops} loops")

    times = timeit.repeat(filter_code3, repeat=loops, number=1, setup=setup_code)
    time_taken = min(times);   stdev_time = statistics.stdev(times);    total_time = sum(times)
    print("Best time for FSRCNN:", f"{time_taken * 1e6:.1f} μs ± \t{stdev_time * 1e6:.1f} μs total of "f"{total_time}  in "f"{loops} loops")
    
    times = timeit.repeat(filter_code4, repeat=loops, number=1, setup=setup_code)
    time_taken = min(times);   stdev_time = statistics.stdev(times);    total_time = sum(times)
    print("Best time for LapSRN:", f"{time_taken * 1e6:.1f} μs ± \t{stdev_time * 1e6:.1f} μs total of "f"{total_time}  in "f"{loops} loops")

    times = timeit.repeat(filter_code5, repeat=loops, number=1, setup=setup_code)
    time_taken = min(times);   stdev_time = statistics.stdev(times);    total_time = sum(times)
    print("Best time for ESPCN:", f"{time_taken * 1e6:.1f} μs ± \t{stdev_time * 1e6:.1f} μs total of "f"{total_time}  in "f"{loops} loops")

    times = timeit.repeat(filter_code6, repeat=loops, number=1, setup=setup_code)
    time_taken = min(times);   stdev_time = statistics.stdev(times);    total_time = sum(times)
    print("Best time for FSRCNN:", f"{time_taken * 1e6:.1f} μs ± \t{stdev_time * 1e6:.1f} μs total of "f"{total_time}  in "f"{loops} loops")
#test_7_3()



