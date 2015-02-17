#Find the most frequent integer in an array
import sys

inputValue = sys.argv[1]
inputArray = inputValue.split(',')

sortedInput = sorted(inputArray)
maxOccurences = 0
numTotal = 0
mostSeenInteger = -1
for i in range(0, len(sortedInput)-1):
	if sortedInput[i] == sortedInput[i+1]:
		numTotal+=1
	else:
		numTotal = 0

	if numTotal > maxOccurences:
		maxOccurences = numTotal
		mostSeenInteger = sortedInput[i]

	print str(numTotal)

print mostSeenInteger
