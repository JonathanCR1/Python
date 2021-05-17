#Entrada de datos: rostros-
import cv2
import os

ruido=cv2.CascadeClassifier('C:\Github\Python\Modelos\data\haarcascades\haarcascade_frontalface_default.xml')

camara=cv2.VideoCapture(0)

while True:
    _ , vivo = camara.read()
    gray=cv2.cvtColor(vivo, cv2.COLOR_BGR2GRAY)
    cara=ruido.detectMultiScale(gray,1.3,5)
    for(x,y,e1,e2) in cara:
        cv2.rectangle(vivo, (x, y), (x+e1,y+e2), (0,254,0),2)
    cv2.imshow("Vivo" , vivo)
    if cv2.waitKey(1)==ord("q"):
        break

camara.release()
cv2.destroyAllWindows()




