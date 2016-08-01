class Node:
	"""A linkedlist node."""
	def __init__(self, value, next=None):
		self.value = value
		self.next = next


def contains_cycle(node):
	"""Return True if the linkedlist starting at 'node'
	has a cycle.

	"""
	# Linkedlist is empty, or has only one node
	if node is None or node.next is None:
		return False

	# Move two pointers at two different rates and
	# check if they ever collide. If yes, there is
	# a cycle in the linkedlist.
	slow = node
	fast = node.next
	while slow != fast:
		try:
			slow = slow.next
			fast = fast.next.next
		# If there is a cycle, we will never
		# encounter a None.
		except AttributeError:
			return False
	return True

if __name__ == "__main__":
	node = Node(1, Node(2, Node(3, Node(4))))
	node.next.next.next.next = node
	print contains_cycle(node) # True
