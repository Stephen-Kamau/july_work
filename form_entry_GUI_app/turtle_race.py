#A racing game for the turtle
from turtle import*
from random import randint
def race_turtle():
	#take the pen up
	penup()
	#move to position x,y
	goto(-140,140)
	for step in range(6):
		speed(10)
		write(step)
		right(90)
		forward(10)
		pendown()
		forward(150)
		penup()
		backward(160)
		left(90)
		forward(20)
		x=Turtle()
		x.color('red')
		x.shape("turtle")
		x.penup()
		x.goto(-160,102)
		x.pendown()
		y=Turtle()
		y.color('blue')
		y.shape("turtle")
		y.penup()
		y.goto(-160,72)
		for i in range(100):
			x.forward(randint(1,5))
			y.forward(randint(1,5))

race_turtle()