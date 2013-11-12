#!/usr/bin/env python


## STANDARD IMPORTS
# ++++++++++++++++++++
# import math as PYMATH; # alias
# from math import *; # import everything
import math 

## MAIN PROGRAM

# if( __name__ == "__main__" ):
# 	 print( "\"Hello\"" );print('Hi')

# strWordToPrint = int( raw_input("What do you want to say?: ") );
# asciiWordToPrint = ord(strWordToPrint);
# print( asciiWordToPrint );
# print( type(asciiWordToPrint) );

# myDict = { "A": "apple",
# 			"B": "ball"};

# print( myDict["A"])

# myList = [ 0, 1, 2, 3, 4 ];

# for i in range( 0, myList.__len__(), 1 ):
# 	print( i );
# 	myList[i] += 1;

# #rof

# print( myList );
def binomialCoeff( n, k ):
	b = (math.factorial(n)/(math.factorial(k)*math.factorial(n - k)));
	return(b);
#fed ++++++++++++++++++++++++++++++++++++++++++


## MAIN PROGRAM

if( __name__ == "__main__" ):
	b = binomialCoeff(n= 2,k= 1);

	print( "B is: " + str(b) );

#fi

## END OF FILE