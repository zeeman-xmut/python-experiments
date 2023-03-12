# -*- coding: utf-8 -*-
import turtle as t
import cv2

t.getscreen().colormode(255)
img = cv2.cvtColor(cv2.imread('./image.jpg')[0: -2: 2], cv2.COLOR_BGR2RGB)
width = len(img[0])
height = len(img)

t.speed(10)
t.delay(0)
t.penup()
t.goto(-width / 4 + 10, height / 2 - 10)
t.pendown()
t.tracer(2000)
for k1, i in enumerate(img):
    for j in i[::2]:
        t.pencolor((j[0], j[1], j[2]))
        t.forward(1)
    t.penup()
    t.goto(-width / 4 + 10, height / 2 - 10 - k1 - 1)
    t.pendown()
t.done()
