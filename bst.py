class NodeNotFound(Exception):
	pass

class Node:
	def __init__(self, value, left=None, right=None):
		self.value = value
		self.left = left
		self.right = right


class BST:
	def __init__(self, root=None):
		self.root = root

	def insert(self, *values):
		for v in values:
			self._insert(v)
		return self

	def _insert(self, value):
		prev = None
		curr = self.root
		while curr is not None:
			prev = curr
			curr = curr.right if value > curr.value \
				else curr.left

		# Empty tree
		if prev is None:
			self.root = Node(value)
			return

		# Non-empty tree
		if value > prev.value:
			prev.right = Node(value)
		else:
			prev.left = Node(value)

	def delete(self, value):
		parent = None
		curr = self.root
		while curr is not None:
			if value == curr.value:
				replacement = self._replacement(curr)
				if replacement is not None:
					self.delete(replacement)
					curr.value = replacement
				else:
					self._unlink(parent, curr)
				return
					
			elif value > curr.value:
				parent = curr
				curr = curr.right
			else:
				parent = curr
				curr = curr.left
		raise NodeNotFound(value)

	@staticmethod
	def _replacement(node):
		if node.left is not None:
			node = node.left
			while node.right is not None:
				node = node.right
			return node.value
		elif node.right is not None:
			node = node.right
			while node.left is not None:
				node = node.left
			return node.value
		else:
			return None

	@staticmethod
	def _unlink(parent, child):
		if child.value > parent.value:
			parent.right = None
		else:
			parent.left = None

	def inorder(self):
		inorder(self.root)

	def preorder(self):
		preorder(self.root)

	def postorder(self):
		postorder(self.root)

	def level_order(self, level):
		BST._level_order(self.root, level)

	@staticmethod
	def _level_order(node, level):
		if node is None or level < 1:
			return
		if level == 1:
			print node.value
			return
		BST._level_order(node.left, level-1)
		BST._level_order(node.right, level-1)

def inorder(node):
	if node is None:
		return
	inorder(node.left)
	print node.value
	inorder(node.right)

def preorder(node):
	if node is None:
		return
	print node.value
	preorder(node.left)
	preorder(node.right)

def postorder(node):
	if node is None:
		return
	postorder(node.left)
	postorder(node.right)
	print node.value

if __name__ == "__main__":
	t = BST().insert(5, 3, 2, 1, 4, 10, 8, 12, 11, 13)
	#t.inorder()
	#t.preorder()
	#t.postorder()
	t.delete(5)
	t.inorder()
	t.level_order(3)
