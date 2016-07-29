class DoublyNode:
	def __init__(self, value, left=None, right=None, parent=None):
		self.value = value
		self.left = left
		self.right = right
		self.parent = parent
		if left is not None:
			self.left.parent = self
		if right is not None:
			self.right.parent = self


class Tree:
	def __init__(self, root):
		self.root = root

	def inorder(self):
		Tree._inorder(self.root)

	@staticmethod
	def _inorder(node):
		if node is None:
			return
		Tree._inorder(node.left)
		print node.value
		Tree._inorder(node.right)

	@staticmethod
	def successor(node):
		if node.right is not None:
			return Tree._left_most(node.right)
		if node.parent is None:
			return None
		if node == node.parent.left:
			return node.parent.value
		while True:
			node = node.parent
			if node.parent is None:
				return None
			if node == node.parent.left:
				return node.parent.value

	@staticmethod
	def _left_most(node):
		while node.left is not None:
			node = node.left
		return node.value


if __name__ == "__main__":
	one = DoublyNode(1)
	three = DoublyNode(3)
	five = DoublyNode(5)
	two = DoublyNode(2, one, three)
	six = DoublyNode(6, five)
	four = DoublyNode(4, two, six)

	tree = Tree(four)
	print Tree.successor(three)
