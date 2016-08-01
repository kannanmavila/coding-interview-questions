class Node:
	"""A linkedlist node."""
	def __init__(self, value, next=None):
		self.value = value
		self.next = next


class InvalidIndex(IndexError):
	pass


class NotEnoughNodes(IndexError):
	pass


def kth_to_last_node(k, node):
	if k <= 0:
		raise InvalidIndex(k)

	first = node
	second = node

	# Try moving second forward 'k' times
	for i in xrange(k):
		try:
			second = second.next
		except AttributeError:
			# Not enough nodes
			raise NotEnoughNodes(k)

	# Move forward together
	while second is not None:
		second = second.next
		first = first.next

	# Now first is at kth-from-last node
	return first.value

if __name__ == "__main__":
	node = Node(1, Node(2, Node(3, Node(4))))
	print kth_to_last_node(2, node) # 3
