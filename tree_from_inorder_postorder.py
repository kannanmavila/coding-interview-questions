class Node(object):
	def __init__(self, value, left=None, right=None):
		self.value = value
		self.left = left
		self.right = right


def binary_tree(inorder, postorder):
	"""Return the root node to the BST represented by the
	inorder and postorder traversals.

	"""
	# Utility for recursively creating BST for
	# a subset of the traversals.
	def _construct(left, right, head_pos):
		if left > right:
			return None

		# Split the inorder array, using head
		# as pivot. `head_pos` is the position
		# of the head in `postorder`.
		pivot = inorder.index(postorder[head_pos])
		head = Node(inorder[pivot])

		# Recursively create subtrees, and connect
		# them to the head.
		head.left = _construct(left, pivot-1,
				head_pos - (right-pivot) - 1)
		head.right = _construct(pivot+1, right,
				head_pos-1)
		return head

	n = len(inorder)
	return _construct(0, n-1, n-1)

def inorder(node):
	if node is None:
		return ""
	return inorder(node.left) + " " + str(node.value) \
			+ inorder(node.right)

def postorder(node):
	if node is None:
		return ""
	return postorder(node.left) + postorder(node.right) \
			+ " " + str(node.value)

if __name__ == "__main__":
	ino = [4, 8, 2, 5, 1, 6, 3, 7]
	post = [8, 4, 5, 2, 6, 7, 3, 1]
	root = binary_tree(ino, post)
	print inorder(root)
	print postorder(root)

	ino = [1, 2, 3]
	post = [3, 2, 1]
	root = binary_tree(ino, post)
	print inorder(root)
	print postorder(root)
