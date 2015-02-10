import itertools
import sys

inputString = sys.argv[1]
sortedString = sorted(inputString)
allCombinations = itertools.permutations(list(sortedString))

combinationList = list(enumerate(allCombinations))
combinations = []
for item in combinationList:
	combinations.append(item[1])

sortedPermutations = sorted(set(combinations))
for index, sequence in enumerate(sortedPermutations):
	joined = ''.join(sequence)
	if joined == inputString:
		print str(index + 1) + '/' + str(len(sortedPermutations))
