#!/usr/bin/python -tt

"""" a short script comparing the value of a to b and return a value 
based upon the comparison""""

def compare(a,b):
	if a > b:
		return 1
	elif a == b:
		return 0 
	elif a < b: 
		return - 1
			

if __name__ == '__main__':
	print compare(5,6)