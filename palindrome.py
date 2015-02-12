#Check if String is a palindrome
import sys

inputValue = sys.argv[1]
charList = list(inputValue)

def isPalindrome(charList):
	for i in range(0, len(charList)/2):
		if charList[i] != charList[len(charList)-1-i]:
			return False
	
	return True

print isPalindrome(charList)
