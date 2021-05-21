#Uso de la camara del movil (1) o uso de la camara web del pc(0)
#Para usar la de movil se usa el "droid cam"
#Importante libreria CV2 para el trato de imagenes 
import cv2

#carga de la imagen en memoria
captura=cv2.VideoCapture(1)

if not captura.isOpened():
    print("No se ha encontrado una camara")
    exit()

while True:
    _,vivo=captura.read()
    #paso a grises la imagen
    gray=cv2.cvtColor(vivo,cv2.COLOR_BGR2GRAY)
    #Mostrar por pantalla la camara del movil
    cv2.imshow("Directo", vivo)
    if cv2.waitKey(1)==ord("q"):
        break
captura.release()
cv2.destroyAllWindows()

