from turtle import*
import turtle


 #configuracion del tamaño de la ventana
setup(1000,1000,0,0)#tamaño de la ventana en donde graficaremos
title("Mosaico con poligonos regulares") #titulo que queremos que se imprima 
bgcolor('red')#color de fondo
screensize(2000,2000)#tamalño del area del dibujo

t=turtle.Turtle() #inicializamos nuestra turtle
t.speed(10)

#funcion para pintar poligonos regulares recibe el largo del lado y la cantidad de lados que va a tener la figura
def pintafigura(lado, n): 
    for i in range(n):
        t.forward(lado)
        t.left(360/n)

#funcion para imprimir circulos 
def circulos():
    for i in range(10,150,5):
        t.pencolor("yellow")
        t.pensize(5)
        t.circle(i)
        t.right(180)

def espiralTriangulos():
    t.pendown()
    for i in range(10,200,5): #intervalo del tamaño en el que empezamos hasta el tamaño a terminar y de cuanto en cuanto avanzamos:
        pintafigura(i,3)
        t.pencolor("blue")
        t.left(40)
        t.pensize(5)

def espiralpenta():
    t.pendown()
    for i in range(10,200,5): #intervalo del tamaño en el que empezamos hasta el tamaño a terminar y de cuanto en cuanto avanzamos:
        pintafigura(i,3)
        t.pencolor("green")
        t.right(40)
        t.pensize(5)


__name__='__main__'
circulos()
espiralTriangulos()
espiralpenta()
mainloop()       
