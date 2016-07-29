
from tree import Node, Tree

def find_paths_with_sum(tree, sum):
	_find_paths_with_sum(tree.root, sum, [])

def _find_paths_with_sum(node, sum, path):
	if node is None:
		return
	path.append(node.value)
	_print_sum_paths(list(path), sum)
	_find_paths_with_sum(node.left, sum, path)
	_find_paths_with_sum(node.right, sum, path)
	path.pop()
	
def _print_sum_paths(path, sum):
	agg = 0
	sum_path = []
	while path:
		curr = path.pop()
		sum_path.append(curr)
		agg += curr
		if agg == sum:
			print " : ".join(map(str, sum_path[::-1]))

def create_random_tree(*values):
	if not values:
		return
	values = list(values)
	root = Node(values.pop(0))
	q = [root]
	while q:
		curr = q.pop(0)
		if values:
			curr.left = Node(values.pop())
			q.append(curr.left)
		if values:
			curr.right = Node(values.pop())
			q.append(curr.right)
	return Tree(root)

if __name__ == "__main__":
	tree = create_random_tree(1, -4, 2, -2, 6, 3, 4, 3, 3, 2)
#	for i in range(0, 5):
#		print "level", i
#		tree.level_order(i)
#	print "--------------------"
	for i in range(0, 7):
		print "paths summing up to", i
		find_paths_with_sum(tree, i)
