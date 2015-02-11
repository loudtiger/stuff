#!/usr/bin/python2

import sys

from collections import Counter

def getNumUniqueLetters(s):
	return len(set(s))

def getNumUniquePermutations(n, seen):
	if seen == n:
		print "Removing duplicate."
		n = n.replace(seen, "")
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

def numLettersPriorTo(c, s):
	numLetters = 0
	splitRemainder = list(set(s))
	for char in splitRemainder:
		if c > char:
			numLetters = numLetters + 1
			
	return numLetters

def calculatePosition(s, seen, accumulator):
	if len(s) == 0:
		return accumulator + 1
	else:
		splitWord = list(s)
		firstChar = splitWord[0]
		remainder = ''.join(splitWord[1:])
		seen = seen + firstChar
		numPermutations = getNumUniquePermutations(remainder, seen)
		print "NumPermutations:" + str(numPermutations)
		numIterations = numLettersPriorTo(firstChar, remainder)
		print "NumIterations:" + str(numIterations) + ", " + str(firstChar) + ":" + str(remainder)
		total = numIterations * numPermutations
		print "Total to add:" + str(total)
		#print "Remainder:" + remainder + ", Accumulator: " + str(accumulator)
		#print "----"
		return calculatePosition(remainder, seen, accumulator + total)


inputString = sys.argv[1]
splitWord = list(inputString)
sortedInput = sorted(splitWord)
if splitWord == ''.join(splitWord):
	print '1'
else:
	print calculatePosition(inputString, '', 0)
	

