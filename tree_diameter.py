class Node(object):
	"""A tree node."""
	def __init__(self, value, left=None, right=None):
		self.value = value
		self.left = left
		self.right = right


def diameter(node):
	# Internal function to abstract the recursion details
	def _diameter(node):
		if node is None:
			return 0, 0

		# Recurse to left and right subtrees
		left_dia, left_height = _diameter(node.left)
		right_dia, right_height = _diameter(node.right)

		# If one of the subtrees is of zero height, then
		# this node cannot be used to make a diameter, since
		# two leaf nodes are required to make a diameter.
		dia = (left_height + right_height + 1) \
				if left_height * right_height > 0 \
				else 1

		# Diameter of the tree rooted at this node is the
		# maximum of the following:
		# a. Diameter of the left sub-tree
		# b. Diameter of the right sub-tree
		# c. Sum of the heights of the sub-trees + 1 (this node)
		dia = max(dia, left_dia, right_dia)

		# Height of the tree rooted at this node is the
		# maximum of the heights of the left and right
		# subtree, plus one.
		height = max(left_height, right_height) + 1

		return dia, height
	return _diameter(node)[0]

if __name__ == "__main__":
	root = Node(1, Node(1, Node(1))) # 1
	root = Node(1, Node(1, Node(1), Node(1, Node(1), Node(1))),
			Node(1, None, Node(1, None,
				Node(1, Node(1, Node(1), Node(1)), Node(1))
			))) # 9
	print diameter(root)
