from turtle import*
import turtle


 #configuracion del tamaño de la ventana
setup(680,480,0,0)#tamaño de la ventana en donde graficaremos
title("Primer diseño de turtle") #titulo que queremos que se imprima 
bgcolor('red')#color de fondo
screensize(500,500)#tamalño del area del dibujo

t=turtle.Turtle() #inicializamos nuestra turtle
t.speed(1)
#funcion para pintar poligonos regulares recibe el largo del lado y la cantidad de lados que va a tener la figura
def pintafigura(lado, n): 
    for i in range(n):
        t.pencolor("blue")
        t.forward(lado)
        t.left(360/n)



print("la medida del lado que desea")
medidalado=int(input("ingrese el dato"))

print("ingrese el numero de lados que desea para su figura")
numlados=int(input("ingrese el numero de lados"))

pintafigura(medidalado,numlados)
mainloop()