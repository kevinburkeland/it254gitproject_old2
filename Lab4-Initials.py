#Created by Ryan Rothenbuhler
import turtle
t=turtle.Pen()

#Moving the cursor to the left of the screen
t.penup()
t.backward(300)
t.pendown()

#This is how to draw the letter R
t.circle(180,180)
t.left(90)
t.forward(720)
t.right(180)
t.forward(360)
t.right(145)
t.forward(400)

#Moving the cursor to the right of the screen
t.penup()
t.right(180)
t.forward(400)
t.left(235)
t.forward(350)
t.pendown()

#This is how to draw the second R
t.circle(180,180)
t.left(90)
t.forward(720)
t.right(180)
t.forward(360)
t.right(145)
t.forward(400)
