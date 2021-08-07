#Expresiones aritmeticas


import math
import sys , os
import numpy as np


def ejercicio1():

    a=float(input("a: "))
    b=float(input("b: "))
    c=float(input("c: "))

    operacion=((c+5)*(b**2-3*a*c)*a**2)/(4*a)

    print(f"El resultado de la operacion es el siguiente:  {operacion}")

def ejercicio2():
    x = input("x: ")
    y = input("y: ")
    x, y = y, x
    print(f"el valor de x es : {x} y el valor de y es: {y}")


def ejercicio3():
    r=int(input("Escriba el radio de su circunferencia: "))
    area=math.pi*r**2
    long=2*math.pi*r
    print(f"El area de su circunferencia es: {area:.1f} mientras que la longitud es: {long:.1f}")

def ejercicio4():
    precio=float(input("Que precio tiene que pagar? "))
    descuento=float(input("Descuento a aplicar "))
    pago=precio-((precio*descuento)/100)
    print(f"Usted va a pagar: {pago:.2f}€")


def condicional():
    dato=int(input("ingrese un numero: "))
    if dato>0:
        print(f"Tu valor {dato} es positivo")
    elif dato==0:
        print(f"Tu valor {dato} es 0")
    else:
        print(f"Tu valor {dato} es negativo")

def condicional1():
    a=int(input("Escriba el primer valor: "))
    b=int(input("Escriba el segundo valor: "))

    if (a%2==0) & (b%2==0):
        print(f"Ambos valores son pares")
    elif (a%2==0) & (b%2!=0):
        print(f"{a} es par")
    elif (a%2!=0) & (b%2==0):
        print(f"{b} es par")
    else:
        print("Ninguno es par")

def condicional2():
    a=int(input("Introduce un numero: "))
    b=int(input("Introduce un numero: "))
    c=int(input("Introduce un numero: "))

    if (a>b) & (a>c):
        print(f"El primer numero es el mayor: {a}")
    elif (b>c) & (b>a):
        print(f"El segundo numero es el mayor: {b}")
    elif (c>b) & (c>a):
        print(f"El tercer numero es el mayor: {c}")
    else:
        print(f"El numero mas alto esta duplicado en dos entradas: {a} , {b} , {c}")


def condicional3():

    s1=str(input("Ingresa un nombre a comparar: "))
    s2=str(input("Ingresa un nombre a comparar: "))

    if s1[0]==s2[0] | s1[-1]==s2[-1]:
        print("Los nombres son iguales")
    else:
        print("No se han encontrado coincidencias.")


def condicional4():
    saldo=2000
    opcion=0
    while opcion<=4:
        print(f"1- Ingresar dinero \n" +
              "2- Retirar dinero \n" +
              "3- Mostrar dinero \n" +
              "4- Salir")
        opcion=int(input("Que operacion desea relizar? "))
        if opcion==1:
            ingreso=float(input("Que cantidad desea ingresar? "))
            saldo+=ingreso
        elif opcion==2:
            retiro=float(input("Que cantidad desea retirar? "))
            if retiro>saldo:
                print("Saldo insuficiente")
            else:
                saldo-=retiro
        elif opcion==3:
            print(f"Saldo disponible: {saldo}")
        elif opcion==4:
            sys.exit()
        else:
            print("No ha seleccionado un valor valido para el menu del banco")

def listas():
    array=[5,9,23,3,6,1]
    array.sort(reverse=True)
    print(array)


def bucles():
    
    numero=int(input("Escriba un numero: "))

    while numero < 0:
        print("ERROR++ El numero no es positivo ")
        numero=int(input("Escriba un numero positivo: "))

    print(f"El resultado de la raiz cuadrada es: {math.sqrt(numero):.2f}")


def forbucles():
    
    for i in [1, 2, 23, 24 , 2 , 4, 6]:
        print(i)

def for1():
    total=0
    for i in range(100):
        total=total+i
        print(total)
    
def conjuntos():
    a={1, 2, 3, 4}
    b={2, 3, 5, 6}
    c={3, 4, 6, 7}

    #Funciones que unen los dos conjuntos
    print("UNIONES")
    print(a|b)
    print(a|c)
    print(b|c)

    #Funciones que te dan las intersecciones(los valores que tienen iguales)
    print("INTERSECCIONES")
    print(a&b)
    print(a&c)
    print(b&c)

    #Funciones que te dan los que tiene el primer parametro distinto del segundo
    print("VALORES IGUALES DE LOS CONJUNTOS")
    print(a-b)
    print(a-c)
    print(b-c)

    #Funciones de diferencias simetricas
    print("DIFERENCIAS SIMETRICAS")
    
    print(a^b)
    print(b^c)
    print(c^a)




def areapx(diametro):
    apx=(((((diametro/2)**2)*np.pi)*10.5)/480)*1000
    return round(apx,2)

centimo_1=areapx(16.26)
centimo_2=areapx(18.75)
centimo_5=areapx(21.25)
centimo_10=areapx(19.75)
centimo_20=areapx(22.25)
centimo_50=areapx(24.25)
euro_1=areapx(23.25)
euro_2=areapx(25.75)


def cursopythonmaster():
    numero=int(input("pon un numero: "))
    resultado = numero >= 18 
    if resultado:
        print("mayor de edad ")
    else:
        print("menor de edad")
cursopythonmaster()

