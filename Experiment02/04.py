# -*- coding: utf-8 -*-
import turtle

t = turtle.Pen()
coordinates_x = (-110, 0, 110, -55, 55)
coordinates_y = (-25, -25, -25, -75, -75)
colors = ("red", "blue", "green", "yellow", "black")
t.pensize(5)
t.speed(10)
for i in range(0, 5):
    t.penup()
    t.goto(coordinates_x[i], coordinates_y[i])
    t.pendown()
    t.pencolor(colors[i])
    t.circle(45)
turtle.done()
