class Node(object):
	def __init__(self, value, left=None, right=None):
		self.value = value
		self.left = left
		self.right = right


def print_merged(root1, root2):
	"""Print BSTs rooted at 'root1' and 'root2', in merged
	sorted order.

	"""
	# Utility to traverse BST in order
	def _traverse(stack, current):
		while True:
			if current is None:
				# If the BST has already been traversed,
				# stack will be empty
				return stack.pop() if stack else None
			stack.append(current)
			current = current.left

	# Traverse both BSTs in order. At each step, print the
	# minimal "current" value, and advance (traverse) in the
	# respective tree.
	stack1 = []
	stack2 = []
	n1 = _traverse(stack1, root1)
	n2 = _traverse(stack2, root2)

	while True:
		# Done printing both BSTs
		if n1 is None and n2 is None:
			return

		# Done printing first BST
		if n1 is None:
			print n2.value
			n2 = _traverse(stack2, n2.right)

		# Done printing second BST
		elif n2 is None:
			print n1.value
			n1 = _traverse(stack1, n1.right)

		# Compare the two "current" nodes, print minimal
		# and advance the corresponding BST
		elif n1.value <= n2.value:
			print n1.value
			n1 = _traverse(stack1, n1.right)
		else:
			print n2.value
			n2 = _traverse(stack2, n2.right)

if __name__ == "__main__":
	root1 = Node(3, Node(0, Node(-1), Node(1.5)), Node(4))
	root2 = Node(2, Node(1))
	print_merged(root1, root2) # -1 0 1 1.5 2 3 4
