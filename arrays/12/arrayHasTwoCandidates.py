#given an array A[] of n numbers and another number x, determine whether 
#or not there exist two elements in S whose sum is exactly x. 

def arrayHasTwoCandidates(array, x):
	sortedArray = sorted(array) #maybe they will ask you to sort it...
	left = 0
	right = len(sortedArray)-1
	while(left < right):
		if sortedArray[left] + sortedArray[right] == x:
			return True
		elif (sortedArray[left] + sortedArray[right] < x):
			left+=1
		else:
			right-=1
			
	return False

def arrayHasTwoCandidatesAlt(array, x):
	valuesMap = {}
	for i in range(0, len(array)):
		temp = x-array[i]
		if temp >=0 and valuesMap.get(temp) == True:
			return True
		
		valuesMap[array[i]] = True
	
	return False

print arrayHasTwoCandidatesAlt([1,2,3,4,5], 3)
