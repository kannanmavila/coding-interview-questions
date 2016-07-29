class Node(object):
	def __init__(self, value, next=None):
		self.value = value
		self.next = next


class NodeNotFound(ValueError):
	pass


def swap_nodes(head, a, b):
	"""Swap nodes a and b without swapping data.

	Raises:
		NodeNotFound - if a and/or b is not present.

	"""
	# No swapping possible
	if a == b:
		return head

	def find_node(value):
		prev, node = None, head
		try:
			while node.value != value:
				prev, node = node, node.next
		except AttributeError:
			raise NodeNotFound(value)
		return prev, node

	# Find a, b and their previous nodes
	prev_a, node_a = find_node(a)
	prev_b, node_b = find_node(b)

	# a is head
	if prev_a is None:
		prev_b.next = node_a
		head = node_b
	# b is head
	if prev_b is None:
		prev_a.next = node_b
		head = node_a
	else:
		prev_a.next = node_b
		prev_b.next = node_a

	# Swap
	temp = node_a.next
	node_a.next = node_b.next
	node_b.next = temp

	return head

def print_list(head):
	while head is not None:
		print head.value
		head = head.next
	print "--"

if __name__ == "__main__":
	head = Node(1, Node(2, Node(3, Node(4, Node(5)))))
	print_list(swap_nodes(head, 2, 4)) # 1 4 3 2 5
	head = Node(1, Node(2, Node(3)))
	print_list(swap_nodes(head, 3, 1)) # 3 2 1
	head = Node(1, Node(2))
	#print_list(swap_nodes(head, 2, 4)) # NodeNotFound
	head = Node(1, Node(2))
	print_list(swap_nodes(head, 2, 1)) # 2 1
	head = Node(1, Node(2, Node(3, Node(4, Node(5)))))
	print_list(swap_nodes(head, 2, 3)) # 1 3 2 4 5
