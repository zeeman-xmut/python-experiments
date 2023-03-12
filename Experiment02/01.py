# -*- coding: utf-8 -*-
import turtle

radius = int(input())
count = int(input())
color = input()

turtle.pencolor(color)
for i in range(count):
    turtle.penup()
    turtle.goto(0, -(radius * i))
    turtle.pendown()
    turtle.circle(radius * i)
turtle.done()
