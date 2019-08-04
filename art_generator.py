from turtle import*
from random import*
import tkinter

speed(19)
def random_color():
	red=randint(0,255)
	blue=randint(0,255)
	green=randint(0,255)
	color('red','green','blue')
def random_place():
	penup()
	x=randint(-100,150)
	y=randint(-100,150)
	goto(x,y)
	pendown()
shape("turtle")
def drawrectangle():
	random_color()
	random_place()
	hideturtle()
	length=randint(10,200)
	height=randint(10,200)
	begin_fill()
	forward(length)
	right(90)
	forward(height)
	right(90)
	forward(length)
	right(90)
	forward(height)
	right(90)
	end_fill()
random_place()
random_color()
stamp()
clear()
setheading(0)
for i in range(25):
	drawrectangle()

tkinter.mainloop()