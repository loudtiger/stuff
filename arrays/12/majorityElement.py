#Write a function which takes an array and emits the majority element 
#(if it exists), otherwise prints NONE as follows

def majorityElement(array):
	appearances = {}
	for i in array:
		if i in appearances:
			numAppearances = appearances.get(i)
			appearances[i] = numAppearances + 1
		else:
			appearances[i] = 1
	
	halfcount = len(array)/2
	for key in appearances:
		if appearances.get(key) > halfcount:
			return key
	
	return "NONE"

def majorityElementMooresVoting(array):
	majorityIndex = 0
	majorityCount = 1
	for i in range(1,len(array)):
		if array[majorityIndex] == array[i]:
			majorityCount+=1
		else:
			majorityCount-=1
		if majorityCount == 0:
			majorityIndex = i
			majorityCount = 1
	
	#got the candidate as array[majorityIndex]. Now confirm..
	count = 0
	for i in array:
		if array[majorityIndex] == i:
			count +=1
	if count > len(array)/2:
		return array[majorityIndex]
	else:
		return "NONE"

def majorityElementSorted(array, x):
	numTotal = 0
	maxTotal = 0
	maxElementIndex = -1
	for i in range(0, len(array)-1):
		if array[i] == array[i+1]:
			numTotal+=1
		else:
			numTotal = 0

		if numTotal > maxTotal:
			maxTotal = numTotal
			maxElementIndex = i

	if maxElementIndex != -1 and x == array[maxElementIndex] and maxTotal > len(array)/2:
		return True

	return False

#def majorityElementBinary(array, x):
	#i = binarySearch(array, 0, len(array)-1, x)
	#if i == -1:
		#return False
	#k = l
	#for k in array:
		#if i == k:
			

def binarySearch(array, low, high, x):
	if high > low:
		mid = low + (high-low)/2
		if mid == 0 or x > array[mid-1] and array[mid] == x:
			return mid
		elif x > array[mid]:
			return binarySearch(array, mid+1, high, x)
		else:
			return binarySearch(array, low, mid-1, x)
	
	return -1

#print majorityElementMooresVoting([1,1,1,1,1,1,1,1,2,3,4,5])
print majorityElementSorted([1,2,3,3,3,3,3,3,3,3,3,4], 4)
