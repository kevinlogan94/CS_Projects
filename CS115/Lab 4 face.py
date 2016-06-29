# Lab 4 turtle graphic face prolog
# Author: Kevin Logan
# Section: 10
# Date: September 11, 2012
# Email: kmlo225@g.uky.edu
# Purpose: Have a fully drawn picture of a face
# Preconditions: Enter the specific commands for turtle to draw shapes.
# Postconditions: The turtle program will draw a head, mouth, nose, and a pair of eyes.
# Main Function
#1. input functions to allow turtle to be used.
#2. input turtle screen
#2. input directions so turtle draws a picture of a red head.
#3. Input directions so turtle draws a picture of a yellow nose.
#4. input directions so turtle draws a picture of a green eye on the right.
#5. Input directions so turtle draws a picture of an blue eye on the left.
#6  Input directions so turtle draws a picture of a purple mouth.
#7. Input directions so the window will close when u click again.

import turtle


y = turtle.Turtle()
y.color("red")
y.pensize(3)
y.hideturtle()

y.penup()
y.left(90)
y.forward(100)
y.pendown()
y.left(90)

for i in [1,2,3,4,5,6,7,8,9,10,11,12]:
    y.forward(80)
    y.left(30)

y.penup()
y.home()
y.forward(30)
y.color("green")
y.pendown()



for i in [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40]:
    y.forward(4)
    y.right(10)

y.penup()
y.home()
y.right(180)
y.forward(110)
y.color("blue")
y.pendown()

for i in [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40]:
    y.forward(4)
    y.left(10)

t=turtle.Turtle()
t.hideturtle()
t.pensize(3)
t.penup()
t.color("yellow")
t.right(140)
t.forward(50)
t.pendown()
t.forward(50)
t.left(140)
t.forward(50)

x = turtle.Turtle()
x.hideturtle()
x.pensize(3)
x.penup()
x.right(80)
x.forward(110)
x.pendown()
x.color("purple")

for i in [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40]:
    x.forward(5)
    x.right(5)

turtle.exitonclick()



