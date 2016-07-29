class Node(object):
	def __init__(self, value, left=None, right=None):
		self.value = value
		self.left = left
		self.right = right


def floor(node, key):
	"""Return the largest value in the tree rooted at 'node',
	that is less than or equal 'key.

	"""
	if node is None:
		return

	# Case 1: floor is in the left subtree
	if node.value > key:
		return floor(node.left, key)

	# Case 2: this node is a possible floor. Better floor
	# may be found in the right subtree.
	else:
		better_floor = floor(node.right, key)
		return better_floor if better_floor is not None \
				else node.value

def ceil(node, key):
	"""Return the smallest value in the tree rooted at 'node',
	that is greater than or equal 'key.

	"""
	if node is None:
		return

	# Case 1: ceil is in the right subtree
	if node.value < key:
		return ceil(node.right, key)

	# Case 2: this node is a possible ceil. Better ceil
	# may be found in the left subtree.
	else:
		better_ceil = ceil(node.left, key)
		return better_ceil if better_ceil is not None \
				else node.value

if __name__ == "__main__":
	root = Node(8, None, Node(20, None, Node(25,
			Node(22, None, Node(24)))))
	for i in [8, 20, 25, 22, 24, 7, 26]:
		print "floor(%d):" % i, floor(root, i)
		print "ceil(%d):" % i, ceil(root, i)
