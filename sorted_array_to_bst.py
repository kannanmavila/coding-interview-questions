from bst import BST, Node

def sorted_array_to_bst(array):
	return _sorted_array_to_bst(array, 0, len(array)-1)

def _sorted_array_to_bst(array, left, right):
	if left == right:
		return Node(array[left])
	if left > right:
		return None

	mid = (left + right) / 2
	root = Node(array[mid])
	root.left = _sorted_array_to_bst(array, left, mid-1)
	root.right = _sorted_array_to_bst(array, mid+1, right)
	return root

if __name__ == "__main__":
	array = [0, 1, 2, 3, 4, 5]
	tree = BST(sorted_array_to_bst(array))
	tree.inorder()
