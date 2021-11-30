import cv2
import numpy as np 

img = cv2.imread('flower_input.jpg',0)

Res= np.zeros(img.shape)
Mask= np.ones((55 ,55)) / 3025


rows , cols = img.shape
for i in range(15,rows-15):
    for j in range(15,cols-15):
        if img[i][j] < 150  :
            PImge = img[i-15:i+16 , j-15:j+16]
            Res[i ,j] = np.sum (PImge * Mask)
        else :
            Res [i,j] = img[i][j]


#cv2.imshow('output.jpg',Res)
cv2.imwrite('Flower,jpg' , Res)
cv2.waitKey()
