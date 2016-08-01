class Node:
    def __init__(self, value):
        self.value = value
        self.left  = None
        self.right = None

    def insert_left(self, value):
        self.left = Node(value)
        return self.left

    def insert_right(self, value):
        self.right = Node(value)
        return self.right


def validate(node, lower=-float('inf'), upper=float('inf')):
	"""Return True if the binary tree rooted at 'node' is
	a valid BST.

	"""
	if node is None:
		return True

	# Violation
	if node.value < lower or node.value > upper:
		return False

	# Recurse
	return validate(node.left, lower, node.value) and \
			validate(node.right, node.value, upper)

def inorder(node):
	if node is None:
		return
	inorder(node.left)
	print node.value
	inorder(node.right)

if __name__ == "__main__":
	tree = Node(5)
	tree.insert_left(3)
	tree.insert_right(8)
	tree.left.insert_left(2)
	tree.left.insert_right(4)
	tree.left.left.insert_left(1)
	tree.right.insert_left(7)
	tree.right.left.insert_left(6)
	#inorder(tree)
	print validate(tree) # True
