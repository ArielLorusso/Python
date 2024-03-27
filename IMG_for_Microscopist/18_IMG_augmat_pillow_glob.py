from PIL import Image  # https://pillow.readthedocs.io/en/stable/reference/index.html
# We are using the main module usefull for data augmentation in machine learning
# IMPORT MODULES  ImageDraw  ImageChops  ImageEnhance  ImageFilter


path = "/home/ariel/Desktop/download.jpg"
img  = Image.open(path)
print(img.size)

# DOWN-SCALE
img_small = img.resize((25,25))
img_small.show(); img.show() # diferent images not a pointer to file
#img_small.save("/home/ariel/Desktop/download_small.png")

# UP-SCALE
img_upscale = img_small.resize((250,250))
#img_upscale.save("/home/ariel/Desktop/download_upscale.jpg")

# CROP
img_crop    = img_upscale.crop((100,100,120,120))#(ini x,y, final x,y)
#img_crop.save("/home/ariel/Desktop/download_crop.jpg")

# COLAGE
img_colage = img.copy()
img_colage.paste(img_upscale,(10,10)) # img,(x,y) frop top left
img_colage.show()

# ROTATE & FLIP

img_rotate = img.rotate(90) # maintains canvas size     empty pixels turn black
img_rotate = img.rotate(45, expand=True) # adapts canvas to new size
img_rotate = img.transpose(Image.FLIP_LEFT_RIGHT)
img_rotate = img.transpose(Image.FLIP_TOP_BOTTOM)
img_rotate.show() # adapts canvas to new size

# GRAYSCALE
img_gray = img.convert("L") # "L"(Luma) "RGB" & "CMYK."   L = R * 299/1000 + G * 587/1000 + B * 114/1000
img_gray.show()

# AUTOMATISATION 
import glob
path = "/home/ariel/Desktop/IMAGES/*" # *: any file inside folder 
for file in glob.glob(path):
    a = Image.open(file)
    b = a.rotate(45)
    b.show()
    name = file.split(".") # name[0]= "path+name"  name[1] = jpg
    b.save(name[0]+"_rotated.jpg")