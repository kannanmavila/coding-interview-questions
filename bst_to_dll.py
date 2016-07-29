class EmptyTree(ValueError):
	pass


class Node(object):
	def __init__(self, value, left=None, right=None):
		self.value = value
		self.left = left
		self.right = right


def convert_to_dll(node):
	""" Convert the BST rooted at 'node' to a circular
	doubly linked list, and return the head and tail.

	"""
	if node is None:
		raise EmptyTree()

	# Utility for connecting two nodes of a DLL
	def _connect(a, b):
		if a == b:
			return # Do nothing
		a.right = b
		b.left = a

	# Recurse to left and right sub-trees
	try:
		l_min, l_max = convert_to_dll(node.left)
	except EmptyTree:
		l_min = l_max = node
	try:
		r_min, r_max = convert_to_dll(node.right)
	except:
		r_min = r_max = node

	# Connect the left and right DLLs
	_connect(l_max, node)
	_connect(node, r_min)
	_connect(r_max, l_min) # Circular connection

	return l_min, r_max

if __name__ == "__main__":
	root = Node(4, Node(2, Node(1), Node(3)), Node(5))
	root = Node(5, Node(2, None, Node(3)))
	root = Node(5, None, Node(9, Node(7)))
	head, tail = convert_to_dll(root)
	print "In order:"
	while True:
		print head.value
		head = head.right
		if head == tail.right:
			break
	print "In reverse:"
	while True:
		print tail.value
		tail = tail.left
		if tail == head.left:
			break
