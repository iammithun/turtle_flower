# -*- coding: utf-8 -*-
"""
Created on Sat Feb 24 20:51:29 2024

@author: iamrs
"""

import turtle

turtle.bgcolor('black')

turtle.speed(0)
turtle.pensize(2)
turtle.pencolor('blue')

def drawcircle(radius):
    for i in range(36):
        turtle.circle(radius)
        radius -= 4

def drawdesign():
    for i in range(10):
        drawcircle(150)
        turtle.right(36)

drawdesign()
turtle.done()
