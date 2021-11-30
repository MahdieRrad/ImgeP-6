from typing import no_type_check
import cv2 
import numpy as np

img_A=cv2.imread('building.tif',0)
img_A=cv2.resize(img_A,(250,250))
img_B=cv2.imread('building.tif',0)
img_B=cv2.resize(img_B,(250,250))


Res_A=np.zeros(img_A.shape)
Res_B=np.zeros(img_A.shape)
Mask_A=np.array([[-1,0,1],
                 [-1,0,1],
                 [-1,0,1]] )


Mask_B=np.array([[-1,-1,-1],
                 [0,0,0],
                 [1,1,1]] )

row,col=img_A.shape

for i in range(1,row-1):
    for j in range(1,col-1):
        PImge_A=img_A[i-1:i+2,j-1:j+2]
        Res_A[i,j]=np.sum(PImge_A*Mask_A)
        PImge_B=img_B[i-1:i+2,j-1:j+2]
        Res_B[i,j]=np.sum(PImge_B*Mask_B)

cv2.imshow('output.jpg',Res_A)
#cv2.imshow('output.jpg',Res_B)
cv2.imwrite('ResultA.jpg',Res_A)
cv2.imwrite('ResultB.jpg',Res_B)
cv2.waitKey()
