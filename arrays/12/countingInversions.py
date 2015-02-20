def countInverse(array):
	result = [0]*len(array)
	return mergeSort(array, result, 0, len(array)-1)

def mergeSort(array, resultingMerge, left, right):
	inverseCount = 0
	if right > left:
		mid = (right+left)/2
		inverseCount = mergeSort(array, resultingMerge, left, mid)
		inverseCount += mergeSort(array, resultingMerge, mid+1, right)
		
		sumCount = merge(array, resultingMerge, left, mid+1, right)
		inverseCount += sumCount
		
	return inverseCount
	
def merge(array, resultingMerge, left, mid, right):
	i = left
	j = mid
	k = left
	inverseCount = 0
	while i <= mid-1 and j <= right:
		if array[i] <= array[j]:
			resultingMerge[k] = array[i]
			#print "resulting merge:" + str(resultingMerge)
			k+=1
			i+=1
		else:
			resultingMerge[k] = array[j]
			#print "resulting merge:" + str(resultingMerge)
			k+=1
			j+=1
			inverseCount = inverseCount + (mid - i)
	
	print "Exiting while loop:" + str(resultingMerge)
	while i <= mid-1:
		resultingMerge[k] = array[i]
		k+=1
		i+=1
	while j <= right:
		resultingMerge[k] = array[j]
		k+=1
		j+=1
	
	for i in range(left,right+1):
		array[i] = resultingMerge[i]
	
	#print str(array)
	return inverseCount

print countInverse([1,2,5,4,3])
