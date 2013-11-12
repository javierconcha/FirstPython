#!/usr/bin/python2.7 -tt
# Copyright 2012 Javier A. Concha. All Rights Reserved.

import sys

def Hello(name):
	if name == 'Alice' or name == 'Nick':
		print 'Alert: Alice Mode'
		name = name + '???'
	else:
		DoesNotExist(name)
	name = name + '!!!'
	print 'Hello', name

# Define a main() function that prints a little greeting.
def main():
	Hello(sys.argv[1])

# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':

	main()