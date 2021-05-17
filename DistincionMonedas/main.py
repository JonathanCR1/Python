from cv2 import cv2
imagen=cv2.imread('C:\Github\Python\DistincionMonedas\/test.jpg')
grey=cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
_,umbral=cv2.threshold(grey,100,255,cv2.THRESH_BINARY )
contornos,jerarquia=cv2.findContours(umbral,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(imagen,contornos,-1,(255 ,0,0),5)

 
cv2.imshow('imagen',grey)
cv2.imshow('imagen original',imagen)
cv2.imshow('umbral',umbral)

cv2.waitKey(0)
cv2.destroyAllWindows()