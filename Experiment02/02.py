# -*- coding: utf-8 -*-
import turtle

t = turtle.Pen()
t.color("yellow", "red")
t.pensize(10)

t.penup()
t.goto(-130.1, 0)
t.pendown()
t.begin_fill()
for i in range(5):
    t.forward(100)
    t.left(72)
    t.forward(100)
    t.right(144)
t.end_fill()
turtle.done()
