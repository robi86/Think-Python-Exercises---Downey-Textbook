#!/usr/bin/python

import sys
import os
import math

def area(radius):
	return math.pi * radius**2

def distance (x1, x2, y1, y2): 
	dx = x2 - x1
	dy = y2 - y1
	dsqaured = dx**2 + dy**2
	hypotenuse = math.sqrt(dsquared)
	print hypotenuse
		
def area_circle(xc, yc, xp, yp):
	cirle_radius = distance(xc, yc, xp, yp)
	return area(circle_radius)
	