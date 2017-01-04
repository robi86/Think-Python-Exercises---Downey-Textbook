#!/usr/bin/python

""" A short script to answer whether values a,b,c will be able to create 
a triangle based upon the lengths provided by the user"""

import math
import sys
import os

def is_triangle(a, b, c): 
	if (a + b > c) and (a + c > b) and (b + c > a):
		print "Yes"
	else:
		print "No"

# prompt the user to enter values for a,b,c

def prompt_user():
	prompt = "Please enter.."
	for value in ("a", "b", "c"):
		new_prompt = prompt + value + '\n'
		input = raw_input(new_prompt)
		float_input = float(input)
		
		""" important to use the 'exec' function to simultanesouly run through the loop
		and also transform the input a,b, and c into a float object"""
		exec("%s=%f" % (value, float_input))
	is_triangle(a,b,c) 

def main():
	prompt_user()
	
if __name__ == '__main__':
   main()