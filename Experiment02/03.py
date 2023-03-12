# -*- coding: utf-8 -*-
import turtle as t

n = int(input())

t.penup()
t.goto(-350, 0)
t.pendown()

t.pensize(2)
t.color("blue", "yellow")

t.begin_fill()
for i in range(3, n + 1):
    t.circle(50, steps=i)
    t.forward(100)
t.circle(50)
t.end_fill()
t.done()
