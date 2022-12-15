from turtle import*
import turtle


 #configuracion del tamaño de la ventana
setup(680,480,0,0)#tamaño de la ventana en donde graficaremos
title("Primer diseño de turtle") #titulo que queremos que se imprima 
bgcolor('pink')#color de fondo
screensize(300,300)#tamalño del area del dibujo

t=turtle.Turtle()
t.speed(1)

def ovalo(rad):
    for i in range(2):
        t.circle(rad,90)
        t.circle(rad//2,90)
    

ovalo(50)    

mainloop()