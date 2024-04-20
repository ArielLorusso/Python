
import numpy as np
import cv2
import os

img = "img/lara.png"    # MUST BE IN DITECTORY : cd OpenCv


model_folder = '/home/ariel/Pictures/'
# model  = "EDSR_x2.pb"    # "edsr", 2   SLOW
# model1 = "EDSR_x3.pb"    # "edsr", 3
model_f2 , model_n2 = "ESPCN_x2.pb" , ("espcn", 2) # FAST + precise
model_f3 , model_n3 = "ESPCN_x4.pb" , ("espcn", 4) #        precise
model_f4 , model_n4 = "ESPCN_x3.pb" , ("espcn", 3) #        not so precise
model_f5 , model_n5 = "LapSRN_x2.pb", ("lapsrn", 2) 
model_f6 , model_n6 = "FSRCNN_x3.pb", ("fsrcnn", 3) #       Smooth & connected

models = (model_f2, model_f3, model_f4 ,model_f5,model_f6 )
names  = (model_n2, model_n3, model_n4 ,model_n5,model_n6 )

img_low  = cv2.imread(img)      # LOAD & SHOW ORIGINAL
cv2.imshow("ORIGINAL", img_low)
cv2.waitKey(0); 


for model_file ,model_name in zip( models, names) :
    sr = cv2.dnn_superres.DnnSuperResImpl_create()  # PROCESS
    sr.readModel( model_folder + model_file );  
    sr.setModel(model_name[0],model_name[1]); 

    result = sr.upsample(img_low)   # SHOW & SAVE
    cv2.imshow(model_file, result)
    cv2.waitKey(0); 
    new_name = os.path.splitext(img )[0]
    new_name += os.path.splitext(model_file )[0]
    new_name += ".jpg"
    print(new_name)
    cv2.imwrite(new_name,result)

img_last  = cv2.imread("img/laraESPCN_x2.jpg")
sr.readModel( model_folder + "ESPCN_x2.pb" )
sr.setModel("espcn", 2)
result = sr.upsample(img_last)   # SHOW & SAVE
cv2.imwrite(os.path.splitext(img )[0]+"laraESPCN_x2x2.jpg",result)
