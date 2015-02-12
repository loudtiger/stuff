class Node():
	def __init__(self, val):
		self.value = val
		self.left = None
		self.right = None
		self.parent = None
	
	def setLeft(self, node):
		self.left = node
		self.left.parent = self
	
	def setRight(self, node):
		self.right = node
		self.right.parent = self
	
	def inorder(self):
		if self.left is not None:
			left = self.left.inorder()
		else:
			left = []
		if self.right is not None:
			right = self.right.inorder()
		else:
			right = []
		return left + [self.value] + right

	def depthfirst(self, node):
		if node is not None:
			print node.value
			self.depthfirst(node.left)
			self.depthfirst(node.right)

	def levelorder(self, node):
		h = self.height(node)
		for i in range(0, h + 1):
			self.printALevel(node, i)
	
	def printALevel(self, node, level):
		if node is None:
			return 0
		if level == 1:
			print node.value
		elif level > 1:
			self.printALevel(node.left, level-1)
			self.printALevel(node.right, level-1)
		
	def height(self, node):
		if node is None:
			return 0
		else:
			heightLeft = self.height(node.left)
			heightRight = self.height(node.right)
			
			if heightLeft > heightRight:
				return heightLeft + 1
			else:
				return heightRight + 1

if __name__ == '__main__':
	tree = Node(4)
	left = Node(3)
	lefter = Node(5)
	right = Node(6)
	tree.setRight(right)
	left.setLeft(lefter)
	left.setRight(Node(8))
	tree.setLeft(left)
	print "In-order:" + str(tree.inorder())
	print "Height:" + str(tree.height(right))
	tree.printALevel(tree, 2)
	print '---------'
	tree.levelorder(tree)
	print '---------'
	tree.depthfirst(tree)
