class Node(object):
	def __init__(self, value, left=None, right=None):
		self.value = value
		self.left = left
		self.right = right
		self.lis = None


def lis(node):
	"""Return the size of the Largest Independent Subset (LIS)
	of the tree rooted at `node`.

	"""
	# No node; empty subset
	if node is None:
		return 0

	# Memoization
	if node.lis is not None:
		return node.lis

	# Largest subset excluding this node
	lis_exclusive = lis(node.left) + lis(node.right)

	# Largest subset including this node. Cannot include
	# children, node gets lonely, hence includes
	# grandchildren.
	lis_inclusive = 1 # This node
	if node.left is not None:
		lis_inclusive += lis(node.left.left) \
				+ lis(node.left.right)
	if node.right is not None:
		lis_inclusive += lis(node.right.left) \
				+ lis(node.right.right)

	# Memoize and return the largest subset
	node.lis = max(lis_exclusive, lis_inclusive)
	return node.lis

if __name__ == "__main__":
	tree = Node(10, Node(20, Node(40), Node(50, Node(70), Node(80))),
			Node(30, None, Node(60)))
	print lis(tree)
