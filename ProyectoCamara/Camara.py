import cv2
captura=cv2.VideoCapture(0)

if not captura.isOpened():
    print("No se ha encontrado una camara")
    exit()

while True:
    _,vivo=captura.read()
    gray=cv2.cvtColor(vivo,cv2.COLOR_BGR2GRAY)
    cv2.imshow("Directo", vivo)
    if cv2.waitKey(1)==ord("q"):
        break
captura.release()
cv2.destroyAllWindows()

