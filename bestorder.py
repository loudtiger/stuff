#!/usr/bin/python2

import sys

from collections import Counter

def getNumUniquePermutations(n):
	remainderList = list(n)
	letterOccurences = Counter(n)
	denominator = 1
	for letter in letterOccurences:
		denominator = denominator * factorial(letterOccurences.get(letter))
	
	return factorial(len(remainderList))/denominator

def factorial(n):
	if n == 0:
		return 1
	
	return n * factorial(n-1)

def calculatePosition(sortedReferenceList, inputWordList, accumulator):
	sortedIndex,inputIndex = (0,0)
	comparedLetters = {}
	while sortedIndex < len(sortedReferenceList):
		while inputIndex < len(inputWordList):
			if inputWordList[inputIndex] != sortedReferenceList[sortedIndex]:
				if comparedLetters.get(sortedReferenceList[sortedIndex]) != inputIndex:
					#Get the number of permutations WITHOUT including the letter.
					accumulator = accumulator + getNumUniquePermutations(sortedReferenceList[0:sortedIndex] + sortedReferenceList[sortedIndex+1:])
					comparedLetters[sortedReferenceList[sortedIndex]] = inputIndex

				sortedIndex+=1
			else:
				del sortedReferenceList[sortedIndex]
				sortedIndex=0
				inputIndex+=1
	else:
		return accumulator + 1

if len(sys.argv) < 2:
	print 'Please run with a string argument.'
	sys.exit()

inputString = sys.argv[1]
splitWord = list(inputString)
sortedInput = sorted(splitWord)
if inputString == ''.join(sortedInput):
	print '1'
else:
	print calculatePosition(sortedInput, splitWord, 0)
