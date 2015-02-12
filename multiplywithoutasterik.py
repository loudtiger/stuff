#Write a multiply function that multiples 2 integers without using *

import sys

inputValue1 = sys.argv[1]
inputValue2 = sys.argv[2]

n1 = int(inputValue1)
n2 = int(inputValue2)

def multiply(n1, n2):
	total = 0
	for i in range(0, n2):
		total = total + n1

	return total

print multiply(n1, n2)

