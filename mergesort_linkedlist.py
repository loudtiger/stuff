class Node():
	def __init__(self, val):
		self.value = val
		self.nextNode = None

class LinkedList():
	def __init__(self, node):
		self.head = node
		self.end = None
	
	def setNext(self, node):

		self.end.nextNode = 

	def hasNext(self):
		if self.nextNode is not None:
			return True
		
		return False

def merge_sort(l):
	getMiddle(l)

def getMiddle(l):
	slow = l
	fast = l
	previous = LinkedList(-1)
	while fast is not None:
		print fast.value
		fast = fast.nextNode
		previous = slow
		slow = slow.nextNode
	
	return previous.value

l = LinkedList(8)
l.setNext(LinkedList(6)).setNext(LinkedList(5)).setNext(LinkedList(1)).setNext(LinkedList(2)).setNext(LinkedList(3)).setNext(LinkedList(4))

listForm = []
#while l is not None:
#	listForm.append(l.value)
#	l = l.nextNode

#print listForm

print getMiddle(l)
