#!/usr/bin/python

""" A short script to check fermats theorem regarding three integers A, B, C being raised 
to a value n"""

import math
import sys
import os


# a a short function using an equivalence operator to compare the left and right side
def check_fermat(a,b,c, n):
	left_side = pow(a,n) + pow(b, n)
	right_side = pow(c,n)
	if left_side == right_side:
		print "Holy smokes, Fermat was wrong!"
	else:
		print "No that doesn't work."

# Ask the user to provide values for a,b,c, and n"
				
def prompt_user():
	prompt = "Please enter.."
	for value in ("a", "b", "c", "n"):
		new_prompt = prompt + value + '\n'
		input = raw_input(new_prompt)
		float_input = float(input)
			""" important to use the 'exec' function to simultanesouly run through the loop
		and also transform the input a,b, and c into a float object"""
		exec("%s=%f" % (value, float_input))
	check_fermat(a,b,c,n)
	

def main():
	prompt_user()

if __name__ == '__main__':
   main()
    