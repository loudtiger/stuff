#Write fibbonaci recursively
import sys

upTo = sys.argv[1]

def printfibonacciInOrder(n):
	first = 0
	second = 1
	if n > 0:
		nextSum = first + second

def fibonacci(n):
	if n == 0:
		return 0
	if n == 1:
		return 1
	else:
		return fibonacci(n-1) + fibonacci(n-2)

print fibonacci(6)
