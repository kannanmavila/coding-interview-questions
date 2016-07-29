class Node(object):
	def __init__(self, value, left=None, right=None):
		self.value = value
		self.left = left
		self.right = right


def print_verticals(root):
	"""Print vertical slices of the binary tree rooted at 'root',
	from left to right.

	"""
	verticals = {}

	# Utility for preprocessing the tree and splitting
	# it into verticals.
	def _split_vertically(node, hd):
		if node is None:
			return hd + 1 # To find left-most vertical

		verticals.setdefault(hd, []).append(node.value)
		_split_vertically(node.right, hd + 1)
		return _split_vertically(node.left, hd-1)

	# Print verticals
	left_most = _split_vertically(root, 0)
	while True:
		if not left_most in verticals:
			return
		print " ".join(map(str, verticals[left_most]))
		left_most += 1

if __name__ == "__main__":
	root = Node(1,
			Node(2,
				Node(4),
				Node(5)
			),
			Node(3,
				Node(6, None, Node(8)),
				Node(7, None, Node(9))
			)
		)
	print_verticals(root)
