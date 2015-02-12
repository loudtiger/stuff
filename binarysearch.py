#Implement binary search of a sorted array of integers
import sys

inputValue = sys.argv[1]
inputSearch = sys.argv[2]
inputList = inputValue.split(",")
numberToFind = int(inputSearch)

def getMidpoint(rangeStart, rangeEnd):
	diff = rangeEnd-rangeStart
	return rangeStart + diff/2

def binarySearch(inputList, numberToFind, rangeStart, rangeEnd):
	if rangeStart > rangeEnd:
		return
	else:
		middle = getMidpoint(rangeStart, rangeEnd)
		if numberToFind < int(inputList[middle]): #we're in the left half.
			return binarySearch(inputList, numberToFind, rangeStart, middle-1)
		elif numberToFind > int(inputList[middle]):
			return binarySearch(inputList, numberToFind, middle+1, rangeEnd)
		else: #middle = numberToFind
			return middle

print binarySearch(inputList, numberToFind, 0, len(inputList))
