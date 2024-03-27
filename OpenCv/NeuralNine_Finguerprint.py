import os
import cv2
import numpy as np


sample = cv2.imread("SOCOFing/Altered/Altered-Hard/150__M_Right_index_finger_Obl.BMP")
# https://docs.opencv.org/4.x/d7/d60/classcv_1_1SIFT.html 
"""                                 CV :: SIFT   Functions :
    double 	getContrastThreshold ()         void  setContrastThreshold    (double contrastThreshold)=0
    String 	getDefaultName ()               
    double 	getEdgeThreshold ()             void  setEdgeThreshold  (double edgeThreshold)=0
    int 	getNFeatures ()                 void  setNFeatures      (int maxFeatures)=0
    int 	getNOctaveLayers ()             void  setNOctaveLayers  (int nOctaveLayers)=0
    double 	getSigma ()                     void	setSigma (double sigma)=0
    
        INHERIT FROM  CV ::	Feature2D :    
void 	compute (InputArrayOfArrays images, std::vector< std::vector< KeyPoint > > &keypoints, OutputArrayOfArrays descriptors)
int 	defaultNorm    () const
int 	descriptorSize () const
int 	descriptorType () const 
void 	detect (InputArray image, std::vector<KeyPoint>&keypoints, InputArray mask=noArray()) 	    Detects keypoints in an image (first variant) or image set (second variant). More...
void 	detect (InputArrayOfArrays images, std::vector<std::vector<KeyPoint>>&keypoints, InputArrayOfArrays masks=noArray())
void 	detectAndCompute (InputArray image, InputArray mask, std::vector< KeyPoint > &keypoints, OutputArray descriptors, bool useProvidedKeypoints=false)


        INHERIT FROM  CV :: Algorithm () :
void 	clear () 	                                Clears the algorithm state. More...
void 	save  (const String  filename)              const
void 	write (FileStorage &fs, const String &name) const      """     

best_score = 0
filename = None
image = None
kp1,kp2,mp = None, None, None   # Key Points    Descriptors

                                    #  Analize just   first 1000 images
counter = 0
for file in [file for file in os.listdir("SOCOFing/Real")][:1000]:
    fingerprint = cv2.imread("SOCOFing/Real/" + file)
    if counter %10 == 0 :
        print(counter)  # show progress 
    counter += 1
    sift = cv2.SIFT_create() 
    # SIFT = Scale Invariant Feature Transform

    keypoints_1 , descriptor_1 = sift.detectAndCompute(sample, None) 
    keypoints_2 , descriptor_2 = sift.detectAndCompute(fingerprint, None) 

    # K-nearest neigbour  K-D tree data structure   k=2 : 2 nearest neighbours
    matches = cv2.FlannBasedMatcher({'algorithm': 1, 'trees': 10}
                                     ).knnMatch(descriptor_1, descriptor_2, k=2)

    
    match_points = []

    for p,q in matches:
        if p.distance < 0.1 * q.distance :
            match_points.append(p)

    keypoints = 0 
    keypoints = min(len(keypoints_1), len(keypoints_2))


    if len(match_points) / keypoints * 100 > best_score:
        best_score = len(match_points) / keypoints * 100
        filename = file
        image = fingerprint
        kp1, kp2, mp = keypoints_1, keypoints_2, match_points

# keypoints and descriptors to txt                                 # SAVE FILES
np.savetxt("keypoints_sample.txt", [(kp.pt[0], kp.pt[1]) for kp in kp1], fmt='%f')
np.savetxt("descriptors_sample.txt", descriptor_1, fmt='%f')
np.savetxt("keypoints_best_match.txt", [(kp.pt[0], kp.pt[1]) for kp in kp2], fmt='%f')
np.savetxt("descriptors_best_match.txt", descriptor_2, fmt='%f')


print("BEST MATCH: "   + filename)
print("SCORE: " + str(best_score))

result = cv2.drawMatches (sample, kp1, image, kp2, mp, None)        # DRAW MATCHES
result = cv2.resize(result,None , fx=4, fy=4)

cv2.imshow("Result", result)
cv2.waitKey(0)
cv2.destroyAllWindows()