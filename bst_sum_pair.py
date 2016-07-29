class Node(object):
	def __init__(self, value, left=None, right=None):
		self.value = value
		self.left = left
		self.right = right


def sum_pair(root, sum):
	"""Find the pair of nodes in the BST rooted at 'root', that
	sum up to 'sum'. Return None if such a pair doesn't exist.

	"""
	# Sanity check
	if root is None:
		return

	# Utility for traversing the BST in or in reverse order
	def _traverse(stack, current, reverse=False):
		"""Arguments:
			stack - traversal stack
			current - node to begin the traversal at
			reverse - If true, traverses the tree in
				reverse order

		"""
		while True:
			if current is None:
				return stack.pop()
			stack.append(current)
			current = current.right if reverse \
					else current.left

	# Maintain two separate stacks for in order and reverse order
	# traversal of the BST.
	min_stack = []
	max_stack = []
	smaller = _traverse(min_stack, root)
	larger = _traverse(max_stack, root, reverse=True)

	while True:
		# Pair doesn't exist
		if smaller.value > larger.value:
			return None

		new_sum = smaller.value + larger.value

		# Found the pair!
		if new_sum == sum:
			return smaller.value, larger.value

		# Sum is too low
		if new_sum < sum:
			smaller = _traverse(min_stack, smaller.right)

		# Sum is too high
		else:
			larger = _traverse(max_stack, larger.left,
					reverse=True)

if __name__ == "__main__":
	root = Node(17, Node(10, Node(8), Node(12)), Node(20,
			Node(16), Node(25)))
	print sum_pair(root, 37) # 12 25
	print sum_pair(root, 33) # 8 25
	print sum_pair(root, 18) # 8 10
	print sum_pair(root, 45) # 20 25
	print sum_pair(root, 24) # 8 16
	print sum_pair(root, 34) # None
