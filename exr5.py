import cv2 as cv
import numpy as np

Mask = np.ones((71,71)) / 5041
cap = cv.VideoCapture(0)
while True:
    _,Frme = cap.read()
    Frme = cv.resize(Frme,(300,300))
    Frme = cv.cvtColor(Frme,cv.COLOR_BGR2GRAY)
    Frme = cv.equalizeHist(Frme)
    row ,col = Frme.shape

    Res = cv.filter2D(Frme,0,Mask)
    Frme_rec = Frme[row//2:row//2+100,col//2:col//2+100]cv.rectangle(Res,(row//2,col//2),(row//2+100,col//2+100),(0,255,0),4)
    Res[row//2:row//2+100,col//2:col//2+100] = Frme_rec
    
    ColorV = int(np.mean(Frme_rec))
    if ColorV <=60:
        color = "Black"
    elif 80< ColorV <=160:
        color = "Gray"
    elif ColorV > 160:
        color = "White"
        
    cv.putText(Res,f"Color: {color}",(20,80),cv.FONT_ITALIC,0.95,(0,0,0),2)
    cv.imshow('output',Res)
    if cv.waitKey(1) & 0xFF==ord('0'):
        break
