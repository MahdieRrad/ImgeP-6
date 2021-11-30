import cv2
import numpy as np 

img = cv2.imread('lion.png' , 0)
img=cv2.resize(img,(250,250))
Res = np.zeros(img.shape)



Mask   = np.array([[0 , -1 , 0],
                  [-1 , 4 , -1],
                  [0 , -1 ,0]] )

row , col = img.shape

for i in range(1,row-1):
    for j in range(1,col-1):
        Imge = img[i-1:i+2 , j-1:j+2]
        Res[i ,j] = np.sum (Imge * Mask)
    
cv2.imshow('OutPut',Res)
cv2.imwrite('Lion.jpg' , Res)
cv2.waitKey()
