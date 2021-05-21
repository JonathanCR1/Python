#Entrada de datos: rostros-
import cv2
import os
import imutils

modelo='FotosElon'
ruta1='C:/Github/Python/ReconocimientoFacial1'
ruta_final=ruta1+'/'+ modelo

if not os.path.exists(ruta_final):
    os.makedirs(ruta_final)

ruido=cv2.CascadeClassifier('C:\Github\Python\Modelos\data\haarcascades\haarcascade_frontalface_default.xml')
camara=cv2.VideoCapture('C:/Github/Python/ReconocimientoFacial1/ElonMusk.mp4')
id=0


while True:
    respuesta , vivo = camara.read()
    if respuesta==False:break
    vivo=imutils.resize(vivo,width=480)
    gray=cv2.cvtColor(vivo, cv2.COLOR_BGR2GRAY)
    idcapture=vivo.copy()

    cara=ruido.detectMultiScale(gray,1.3,5)

    for(x,y,e1,e2) in cara:
        cv2.rectangle(vivo, (x, y), (x+e1,y+e2), (0,254,0),2)
        rostro=idcapture[y:y+e1,x:x+e2]
        rostro=cv2.resize(rostro, (160,160),interpolation=cv2.INTER_CUBIC)
        cv2.imwrite(ruta_final+"/imagen_{}.jpg".format(id),rostro)
        id+=1

    cv2.imshow("Vivo" , vivo)
    if id==351:
        break

camara.release()
cv2.destroyAllWindows()




