#Given 2 integer arrays, determine if the 2nd array is a rotated version of the 1st array. 
#Ex. Original Array A={1,2,3,5,6,7,8} Rotated Array B={5,6,7,8,1,2,3}
import sys

inputValue1 = sys.argv[1]
inputValue2 = sys.argv[2]
firstArray = inputValue1.split(',')
secondArray = inputValue2.split(',')

def getPivotPosition(firstArray, secondArray):
	for i in range(0, len(firstArray)):
		if firstArray[i] ==  secondArray[0]:
			return i
	
	return -1

def ensureArraysMatch(rotatedFirstArray, secondArray):
	for i in range(0, len(rotatedFirstArray)):
			if rotatedFirstArray[i] != secondArray[i]:
				return False
	
	return True

if len(firstArray) != len(secondArray):
	print False
else:	
	pivotPos = getPivotPosition(firstArray, secondArray)
	if pivotPos > 0:
		rotatedFirstArray = firstArray[pivotPos:] + firstArray[0:pivotPos]
		print ensureArraysMatch(rotatedFirstArray, secondArray)
		
				
