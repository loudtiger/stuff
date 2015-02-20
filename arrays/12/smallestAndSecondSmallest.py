#Write an efficient C program to find smallest and second smallest element in an array.
import sys

def getSmallestAndSecondSmallest(array):
	smallest = sys.maxsize
	secondSmallest = sys.maxsize
	
	for i in array:
		if i < smallest:
			secondSmallest = smallest
			smallest = i
		elif i < secondSmallest and i != smallest:
			secondSmallest = i
		
	return (smallest, secondSmallest)
	

print getSmallestAndSecondSmallest([1,2,3,4,5,6])
