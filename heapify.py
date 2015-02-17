from math import floor

def heapify(array, index, size):
	print "Index:" + str(index) + ", size:" + str(size)
	left = index*2 + 1
	right = index*2 + 2

	if left < size and array[index] < array[left]:
		largestIdx = left
	else:
		largestIdx = index

	if right < size and array[largestIdx] < array[right]:
		largestIdx = right

	print "LargestIdx:" + str(largestIdx) + ", size: " + str(size) + ", left: " + str(left) + ", right: " + str(right)
	if largestIdx != index: #if the index of the largest element is not the index, then we gotta swap.
		print "Swapping " + str(array[largestIdx]) + " and " + str(array[index])
		temp = array[index]
		array[index] = array[largestIdx]
		array[largestIdx] = temp

		heapify(array, largestIdx, size)

def build_heap(array, size):
	length = int(floor(size/2))
	while length >= 0:
		heapify(array, length, size)
		length-=1

def heapsort(array):
	count = len(array)-1
	build_heap(array, count)
	print "Heap built:" + str(array)
	while count > 0:
		temp = array[count]
		array[count] = array[0]
		array[0] = temp
		print "Swapped:" + str(array)
		build_heap(array, count)
		print "Rebuilt heap:" + str(array)
		count-=1

array = [7,9,8]
#print array
#build_heap(array, len(array))
#print array
heapsort(array)
print array
