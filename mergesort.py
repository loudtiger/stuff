def merge_sort(a):
	if not a or len(a) == 1:
		return a # done

	l = len(a)
	half1 = merge_sort(a[0:l/2])
	half2 = merge_sort(a[l/2:])
	asorted = []
	hindex1 = 0
	hindex2 = 0
	while hindex1 < len(half1) and hindex2 < len(half2):
		if half1[hindex1] >= half2[hindex2]:
			print str(half1[hindex1]) + " is >= " + str(half2[hindex2])
			asorted.append(half2[hindex2])
			hindex2+=1
		else:
			asorted.append(half1[hindex1])
			hindex1+=1
	if hindex1 < len(half1): #if we didn't finish looking at everything...just tack it on the end since the other half is done.
		asorted.extend(half1[hindex1:])
	else:
		asorted.extend(half2[hindex2:])

	return asorted

array = [8,7,6,1,5,4,2,3]
print array
print merge_sort(array)
