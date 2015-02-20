#Write an efficient C program to find the largest sum of contiguous subarray 

def kadanesAlgorithm(array):
	maxSoFar = 0
	maxEndingHere = 0
	for i in array:
		maxEndingHere = maxEndingHere + i
		if maxEndingHere < 0:
			maxEndingHere = 0
		if maxSoFar < maxEndingHere:
			maxSoFar = maxEndingHere
		
	return maxSoFar

print kadanesAlgorithm([-1,2,3,9,2,1,1,1,])
