from turtle import*
import turtle


 #configuracion del tamaño de la ventana
setup(680,480,0,0)#tamaño de la ventana en donde graficaremos
title("Primer diseño de turtle") #titulo que queremos que se imprima 
bgcolor('pink')#color de fondo
screensize(500,500)#tamalño del area del dibujo

#trasos con turtle cuadrado
t = turtle.Turtle() #instaciamos un objeto tortuga 
t.speed(1) #velocidad del cursor
t.forward(100)
t.left(90)

t.forward(100)
t.left(90)

t.forward(100)
t.left(90)

t.forward(100)
t.left(90)

t.hideturtle()
mainloop()##mantiene la ventana abierta
