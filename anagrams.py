#Determine if 2 Strings are anagrams
import sys

inputValue1 = sys.argv[1]
inputValue2 = sys.argv[2]

charList1 = list(inputValue1)
charList2 = list(inputValue2)

if ''.join(sorted(charList1)) == ''.join(sorted(charList2)):
	print True
else:
	print False
