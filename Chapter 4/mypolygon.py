#!/usr/bin/python

""" Set of functions based on Think Python Case Study Exercise Turtleworld package 
that uses Swampy module to reference functions Turtleword and Turtle """

import sys
import os
import math

## Import Turtleworld package and call functions from Turtleworld module
from swampy.TurtleWorld import *
world = TurtleWorld()
bob = Turtle()
print bob

## Set Turtle speed
bob.delay = 0.01

def square(t, length):
	for i in range(4):
		fd(t, length)
		lt(t)

def polyline(t, n, length, angle):
	for i in range(n):
		fd(t, length/2)
		lt(t, angle/2)

def polygon(t, n, length):
	angle = 360/n
	polyline(t, n, length, angle)

## Circle function becomes unnecessary with availability of arc function with polyline
## def circle(t, r): 
##	circumference = 2 * math.pi * r
##	n = int(circumference/3) + 1
##	length = circumference / n 
##	polygon(t, n, length)	
## circle(bob, 30)

def arc (t, r, angle): 
	arc_length = 2 * math.pi * r * angle / 360
	n = int(arc_length/3) + 1
	step_length = angle / n
	step_angle = float(angle) / n
	lt(bob, step_angle/2)
	rt(bob, step_angle/2)
	

  # draw a circle centered on the origin
r = 100
pu(bob)
fd(bob, r)
lt(bob)
pd(bob)
polyline(bob, n, step_length, step_angle)


wait_for_user()

if __name__ == '__main__':
    main()