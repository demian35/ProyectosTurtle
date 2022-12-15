from turtle import*
import turtle


 #configuracion del tamaño de la ventana
setup(680,480,0,0)#tamaño de la ventana en donde graficaremos
title("Mosaico con poligonos regulares") #titulo que queremos que se imprima 
bgcolor('red')#color de fondo
screensize(800,800)#tamalño del area del dibujo

t=turtle.Turtle() #inicializamos nuestra turtle
t.speed(3)

#funcion para pintar poligonos regulares recibe el largo del lado y la cantidad de lados que va a tener la figura
def pintafigura(lado, n): 
    for i in range(n):
        t.pencolor("blue")
        t.forward(lado)
        t.left(360/n)

#funcion para pintar un mini mosaico con poligonos regulares
def mosaicoPolRegulares():
    for i in range(3,12):
        pintafigura(100,i)

__name__='__main__'
mosaicoPolRegulares()
mainloop()        