#Find the first non-repeated character in a String
import sys

inputValue = sys.argv[1]
charList = list(inputValue)

def findFirstNonRepeating(charList):
	for i in range(0, len(charList)-1):
		if charList[i] != charList[i+1]:
			return charList[i+1]
	
	return -1
			
print findFirstNonRepeating(charList)
