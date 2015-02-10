import sys

def getNumUniqueLetters(s):
	return len(set(s))

def factorial(n):
	if n == 0:
		return 1
	
	return n * factorial(n-1)

def numLettersPriorTo(c, s):
	numLetters = 0
	splitRemainder = list(s)
	for char in splitRemainder:
		if c > char:
			numLetters = numLetters + 1
			
	return numLetters

def calculatePosition(s, seen, accumulator):
	if len(s) == 1:
		return accumulator + 1
	else:
		splitWord = list(s)
		firstChar = splitWord[0]
		seen = seen + firstChar
		remainder = ''.join(splitWord[1:])
		numRemainingUniqueLetters = getNumUniqueLetters(remainder)
		print "NumUniqueLetters:" + str(numRemainingUniqueLetters) + " from " + remainder
		numPermutations = factorial(numRemainingUniqueLetters)
		print "NumPermutations:" + str(numPermutations)
		numIterations = numLettersPriorTo(firstChar, remainder)
		print "NumIterations:" + str(numIterations) + ", " + str(firstChar) + ":" + str(remainder)
		total = numIterations * numPermutations
		print "Total to add:" + str(total)
		print "Remainder:" + remainder + ", Accumulator: " + str(accumulator)
		print "Seen chars:" + seen
		print "----"
		return calculatePosition(remainder, seen, accumulator + total)
		
inputString = sys.argv[1]
splitWord = list(inputString)
sortedInput = sorted(splitWord)
if splitWord == ''.join(splitWord):
	print '1'
else:
	print calculatePosition(inputString, '', 0)
	

