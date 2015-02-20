#You are given a list of n-1 integers and these integers are in the range of 1 to n. 
#There are no duplicates in list. One of the integers is missing in the list. 
#Write an efficient code to find the missing integer.

def findMissingNumber(array):
	n = len(array)
	total = ((n+1)*(n+2))/2
	print "Total:" + str(total)
	for i in array:
		total-=i
	
	return total

def findMissingNumberXor(array):
	xored = 0
	for i in array:
		xored = xored^i

	properxored = 1
	for i in range(1, len(array)+1):
		properxored = properxored^i
	
	return xored^properxored

print findMissingNumberXor([1,2,3,4,5,7])
