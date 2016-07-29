class Node(object):
	def __init__(self, value, left=None, right=None):
		self.value = value
		self.left = left
		self.right = right

	def __cmp__(self, other):
		return cmp(self.value, other.value)


def get_swapped(root):
	"""Return the two nodes that are swapped in the
	BST rooted at 'root'.

	"""
	# Utility for checking violations
	def _check(node, low, high):
		if node is None:
			return

		# Check to the left swapped[0]
		_check(node.left, low, node)

		# In case low and high themselves are swapped
		low, high = min(low, high), max(low, high)

		# Check at the current node
		if node < low:
			# First finding of violation
			if swapped[0] is None:
				swapped[0] = low
			swapped[1] = node
		elif node > high:
			# First finding of violation
			if swapped[0] is None:
				swapped[0] = node
			swapped[1] = high

		# Finally, check to the right
		_check(node.right, node, high)

	# Check starting from 'root'
	swapped = [None, None]
	_check(root, Node(-float('inf')), Node(float('inf')))
	return swapped[0], swapped[1]

if __name__ == "__main__":
	# Test cases
	roots = []
	roots.append(Node(5, Node(2, Node(3, Node(4, Node(1)))))) # 4 2
	roots.append(Node(1, None, Node(4, None, Node(3, None, Node(2, None,
			Node(5)))))) # 4 2
	roots.append(Node(1, None, Node(2, None, Node(4, None, Node(3, None,
			Node(5)))))) # 4 3
	roots.append(Node(5, Node(10, Node(2), Node(8)), Node(20))) # 10 5
	roots.append(Node(10, Node(5, Node(2), Node(20)), Node(8))) # 20 8
	roots.append(Node(2, None, Node(4, Node(4, Node(1))))) # 2 1

	for r in roots:
		first, second = get_swapped(r)
		print first.value, second.value
