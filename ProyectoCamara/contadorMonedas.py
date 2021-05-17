import cv2
import numpy as np


def areapx(diametro):
    apx=(((((diametro/2)**2)*np.pi)*10.5)/720)*1000
    return round(apx,2)


def ordenarpuntos(puntos):
    n_puntos=np.concatenate([puntos[0],puntos[1],puntos[2],puntos[3]]).tolist()
    y_order=sorted(n_puntos,key=lambda n_puntos:n_puntos[1])
    x1_order=y_order[:2]
    x1_order=sorted(x1_order,key=lambda x1_order:x1_order[0])
    x2_order=y_order[2:4]
    x2_order=sorted(x2_order , key=lambda x2_order:x2_order[0])
    return [x1_order[0],x1_order[1],x2_order[0],x2_order[1]]

def alineacion(imagen, ancho,alto):
    imagen_alineada=None
    grises=cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
    _,umbral=cv2.threshold(grises,150,255,cv2.THRESH_BINARY)
    cv2.imshow("Umbral",umbral)
    contornos=cv2.findContours(umbral,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)[0]
    contornos=sorted(contornos ,key=cv2.contourArea, reverse=True)[:1]
    for i in contornos:
        areas_monedas=0.01*cv2.arcLength(i, True)
        appox=cv2.approxPolyDP(i, areas_monedas,True)
        if len(appox)==4:
            puntos=ordenarpuntos(appox)
            puntos1=np.float32(puntos)
            puntos2=np.float32([[0,0],[ancho,0],[0,alto],[ancho,alto]])
            m = cv2.getPerspectiveTransform(puntos1, puntos2)
            imagen_alineada=cv2.warpPerspective(imagen,m,(ancho,alto))
    return imagen_alineada

video=cv2.VideoCapture(1)

while True:
    tipocamara,vivo=video.read()
    if tipocamara==False:
        break
    imagen_a6=alineacion(vivo,ancho=720,alto=1014)
    if imagen_a6 is not None:
        puntos=[]
        gray=cv2.cvtColor(imagen_a6,cv2.COLOR_BGR2GRAY)
        blur=cv2.GaussianBlur(gray,(5,5),1)
        _,umbral2=cv2.threshold(blur,0,255,cv2.THRESH_OTSU+cv2.THRESH_BINARY_INV)
        #cv2.imshow("Umbral", umbral2)
        cont=cv2.findContours(umbral2, cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)[0]
        cv2.drawContours(imagen_a6,cont,-1, (0,255,0),2)
        centimo_1=areapx(16.26)
        centimo_2=areapx(18.75)
        centimo_5=areapx(21.25)
        centimo_10=areapx(19.75)
        centimo_20=areapx(22.25)
        centimo_50=areapx(24.25)
        euro_1=areapx(23.25)
        euro_2=areapx(25.75)
        suma1=0.0
        suma2=0.0
        suma3=0.0
        suma4=0.0
        suma5=0.0
        suma6=0.0
        suma7=0.0
        suma8=0.0
        for c in cont:
            area=cv2.contourArea(c)
            Momentos = cv2.moments(c)
            if (Momentos["m00"]==0):
                Momentos["m00"]=1.0
            x=int(Momentos["m10"]/Momentos["m00"])
            y=int(Momentos["m01"]/Momentos["m00"])

            if area<centimo_1 and area>(centimo_1-300):
                font=cv2.FONT_HERSHEY_SIMPLEX
                cv2.putText(imagen_a6 , "1 cent." , (x,y), font,0.75,(0,255,0))
                suma1+=0.01
                
            if area<centimo_2 and area>(centimo_2-300):
                font=cv2.FONT_HERSHEY_SIMPLEX
                cv2.putText(imagen_a6 , "2 cent." , (x,y), font,0.75,(0,255,0))
                suma2+=0.02

            if area<centimo_5 and area>(centimo_5-300):
                font=cv2.FONT_HERSHEY_SIMPLEX
                cv2.putText(imagen_a6 , "5 cent." , (x,y), font,0.75,(0,255,0))
                suma3+=0.05


            if area<centimo_10 and area>(centimo_10-300):
                font=cv2.FONT_HERSHEY_SIMPLEX
                cv2.putText(imagen_a6 , "10 cent." , (x,y), font,0.75,(0,255,0))
                suma4+=0.1

            if area<centimo_20 and area>(centimo_20-300):
                font=cv2.FONT_HERSHEY_SIMPLEX
                cv2.putText(imagen_a6 , "20 cent." , (x,y), font,0.75,(0,255,0))
                suma5+=0.2

            if area<centimo_50 and area>(centimo_50-300):
                font=cv2.FONT_HERSHEY_SIMPLEX
                cv2.putText(imagen_a6 , "50 cent." , (x,y), font,0.75,(0,255,0))
                suma6+=0.5

            if area<euro_1 and area>(euro_1-300):
                font=cv2.FONT_HERSHEY_SIMPLEX
                cv2.putText(imagen_a6 , "1€" , (x,y), font,0.75,(0,255,0))
                suma7+=1
        
            if area<euro_2 and area>(euro_2-300):
                font=cv2.FONT_HERSHEY_SIMPLEX
                cv2.putText(imagen_a6 , "2€" , (x,y), font,0.75,(0,255,0))
                suma8+=2
        total=suma1+suma2+suma3+suma4+suma5+suma6+suma7+suma8
        print("Dinero total: ",round(total,2))
        
        cv2.imshow("imagen" , imagen_a6)
        cv2.imshow("Vivo" , vivo)
    if cv2.waitKey(1)==ord("q"):
        break
    video.release()
    cv2.destroyAllWindows()




