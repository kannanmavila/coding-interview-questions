class Node(object):
	def __init__(self, value, left=None, right=None, random=None):
		self.value = value
		self.left = left
		self.right = right
		self.random = random


def clone(root):
	"""Clone the binary tree rooted at 'root', and containing
	"random" pointers to another node, or None.

	"""
	# Utility to construct the clone tree.
	# The original tree is temporarily modified to
	# enable fixing of random pointers.
	def _construct(node):
		if node is None:
			return None

		clone = Node(node.value)
		clone.left = node.left
		node.left = clone # This is the trick!

		# Recurse to left subtree
		_construct(clone.left)

		# Recurse to right subtree
		_construct(node.right)

		return clone

	# Utility for fixing random pointers
	def _fix_random(node):
		if node is None:
			return

		random = node.random
		clone = node.left
		clone.random = random.left if random is not None \
				else None

		# Recurse to subtrees
		_fix_random(clone.left)
		_fix_random(node.right)

	# Utility to revert the temporary modifications made to
	# both the original and the clone tree.
	def _revert(node):
		if node is None:
			return None

		clone = node.left
		node.left = clone.left # Undo the trick

		# Recurse to and connect(!) the subtrees
		clone.left = _revert(node.left)
		clone.right = _revert(node.right)
		return clone

	# Step 1: Create a clone of the tree, "within" the
	# tree (the trick).
	_construct(root)

	# Step 2: Create the random pointers
	_fix_random(root)

	# Step 3: Revert the temporary modifications made to
	# both the trees.
	return _revert(root)

def inorder(node):
	if node is None:
		return

	inorder(node.left)

	print node.value
	random = node.random
	print "->", random.value if random is not None else None

	inorder(node.right)

if __name__ == "__main__":
	root = Node(10, Node(5, Node(2)),
			Node(20, Node(15, None, Node(17)), Node(25)))
	root.random = root
	root.left.left.random = root
	root.right.random = root.right.left.right
	root.right.left.random = root.right.left.right
	root.right.left.right.random = root.right.right
	inorder(root)
	print "-------------"
	dupe = clone(root)
	inorder(dupe)
