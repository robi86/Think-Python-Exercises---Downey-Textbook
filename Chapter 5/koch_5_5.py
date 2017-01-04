#!/usr/bin/python

""" a script using the TurtleWorld module in the Swampy package of Think Python
to draw a Koch pattern/snowlfake using concepts of fractals"""

import sys
import os
import math

try:
    # see if Swampy is installed as a package
    from swampy.TurtleWorld import *
except ImportError:
    # otherwise see if the modules are on the PYTHONPATH
    from TurtleWorld import *
world = TurtleWorld()
bob = Turtle()

bob.delay = 0.01

# prompt the user to enter a length and change this length value to a float

def prompt_user():
	prompt = "Please enter a length"
	new_prompt = prompt + '\n'
	input = raw_input(new_prompt)
	float_input = float(input)
	snowflake(bob, float_input)
	wait_for_user()

# function to tell the the pen where and when to draw/turn
def koch(t, l):
	if l < 3:
		fd(t, l)
		return
	else: 
		koch(t, l / 3)
		""" Note the l/3 is based upon fractal concepts that each side of a 
		triangle is divded into three for each iteration"""
		lt(t, 60)
		koch(t, l / 3)
		rt(t, 120)
		koch(t, l / 3)
		lt(t, 60)
		koch(t, l/3) 

def snowflake(t, l):
	for i in range(3):
		koch(t,l)
		rt(t, 120)
		
def main():
	prompt_user()
			
if __name__ == '__main__':
   main()