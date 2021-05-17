from cv2 import cv2
import numpy as np
var_gauss=1
var_kerner=33

monedas=cv2.imread('C:\Github\Python\DistincionMonedas\/monedas.jpg')
monedas=cv2.imread('C:\Github\Python\DistincionMonedas\/monedassoles.jpg')
gray=cv2.cvtColor(monedas, cv2.COLOR_BGR2GRAY)
desenfoque=cv2.GaussianBlur(gray,(var_gauss,var_gauss),0)
canny=cv2.Canny(desenfoque,60,100)
kernel=np.ones((var_kerner,var_kerner),np.uint8)
cierreContorno=cv2.morphologyEx(canny,cv2.MORPH_CLOSE ,kernel)
contornos,jerarquia=cv2.findContours(cierreContorno.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
#cv2.drawContours(monedas,contornos,-1,(255 ,0,0),5)

 
print("Monedas encontradas: {}".format(len(contornos)))
cv2.drawContours(monedas,contornos,-1,(255 ,0,0),5)
#Muestra de las imagenes
cv2.imshow('MONEDAS ' , monedas)
#cv2.imshow('umbral',umbral)

cv2.waitKey(0)
cv2.destroyAllWindows()