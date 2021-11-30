import cv2
import numpy as np

def Cono(img,var):
    Mask=np.ones((var,var))/var**2
    Res=np.zeros(img.shape)
    row,col=img.shape

    for i in range(var//2,row-(var//2)):
        for j in range(var//2,col-(var//2)):
            PImge=img[i-(var//2):i+1+(var//2),j-(var//2):j+1+(var//2)]
            Res[i,j]=np.sum(PImge*Mask)
    cv2.imwrite('1.jpg',Res)


img=cv2=cv2.imread('pic4.jpg',0)

while True:
    print('choise each one :')
    print('1=> 3*3')
    print('2=> 5*5')
    print('3=> 7*7')
    print('4=> 15*15')
    chs=int(input())
    if chs==1:
        Cono(img,3)
        break
    if chs==2:
        Cono(img,5)
        break 
    if chs==3:
        Cono(img,7)
        break
    if chs==4:
        Cono(img,15)
        break
    else:
        print('Ops....')
        break
