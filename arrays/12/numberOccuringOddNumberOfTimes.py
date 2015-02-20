#Given an array of positive integers. 
#All numbers occur even number of times except one number which occurs odd number of times. 
#Find the number in O(n) time & constant space.

def numberOddTimes(array):
	xored = 0
	for i in array:
		xored = xored^i
	return xored


print numberOddTimes([1,2,3,1,2,3,1])
