#Find the only element in an array that only occurs once.
import sys

inputValue = sys.argv[1]
inputArray = inputValue.split(',')

xor = 0
for k in inputArray:
    xor = xor^int(k)
    #print str(k) + ":"+ str(xor)

print xor
