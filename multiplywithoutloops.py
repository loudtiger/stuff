#Write a multiply function that multiples 2 integers without loops

import sys

inputValue1 = sys.argv[1]
inputValue2 = sys.argv[2]

n1 = int(inputValue1)
n2 = int(inputValue2)

def multiply(n2, accumulator):
	if n2 == 0:
		return accumulator
	else:
		accumulator = accumulator + n1
		return multiply(n2-1, accumulator)

print multiply(n2, 0)
