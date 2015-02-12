#Reverse a String recursively
import sys

inputValue = sys.argv[1]
charList = list(inputValue)

def reverse(charList):
	if len(charList) == 1:
		return charList[0]
	else:
		return charList[len(charList)-1] + reverse(charList[0:len(charList)-1])

print reverse(charList)
