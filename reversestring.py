#Reverse a String iteratively
import sys

inputValue = sys.argv[1]
charList = list(inputValue)

def reverse(charList):
	reverses = []
	i = len(charList)-1
	while i >= 0:
		reverses.append(charList[i])
		i-=1
	
	return ''.join(reverses)

print reverse(charList)
