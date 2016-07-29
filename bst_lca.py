class Node(object):
	def __init__(self, value, left=None, right=None):
		self.value = value
		self.left = left
		self.right = right


def lca(node, a, b):
	"""Find the lowest common ancestor of a & b in the BST
	rooted at 'node'.

	"""
	# Leaf node
	if node is None:
		return None

	if min(a, b) <= node.value <= max(a, b):
		return node.value
	elif node.value < min(a, b):
		return lca(node.right, a, b)
	else:
		return lca(node.left, a, b)

if __name__ == "__main__":
	root = Node(20, Node(8, Node(4), Node(12, Node(10),
			Node(14))), Node(22))
	nodes = [20, 8, 22, 4, 12, 10, 14]
	for i in nodes:
		for j in nodes:
			print "lca(%d, %d) = %d" % (i, j, lca(root, i, j))
