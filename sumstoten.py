#Find pairs in an integer array whose sum is equal to 10 (bonus: do it in linear time)
import sys

inputValue = sys.argv[1]
inputArray = inputValue.split(',')

pairs = []
sortedInput = sorted(inputArray)
i = 0
while i < len(sortedInput):
	lookingFor = 10 - int(sortedInput[i])
	if lookingFor >= 0:
		k = i
		while k < len(sortedInput):
			if lookingFor == int(sortedInput[k]):
				print (sortedInput[i], sortedInput[k])
			k+=1
	i+=1

#how do you do this in linear time?
