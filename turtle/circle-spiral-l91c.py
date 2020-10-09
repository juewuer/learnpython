#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/2/15 21:54
# @Author  : Juewuer @ github.com
# @Site    : 
# @File    : circle-spiral-l91c.py
# @copyright: ksyun


import turtle
t = turtle.Pen()
turtle.bgcolor("black")
turtle.speed('fastest')
colors = ["red", "yellow", "blue", "green"]
print( turtle.speed())
for x in range(100):
    t.pencolor(colors[x%4])
    t.circle(1.2*x)
    t.left(95)

turtle.exitonclick()