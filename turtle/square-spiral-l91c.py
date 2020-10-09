#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/2/15 21:29
# @Author  : Juewuer @ github.com
# @Site    : 
# @File    : square-spiral-l91c.py
# @copyright: ksyun

import turtle
t = turtle.Pen()
colors = ["red", "yellow", "blue", "green"]
for x in range(100):
    t.pencolor(colors[x%4])
    t.forward(x)
    t.left(91)

turtle.exitonclick()
