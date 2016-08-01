class Node:
	"""A linkedlist node."""
	def __init__(self, value, next=None):
		self.value = value
		self.next = next


def reverse(head):
	"""Reverse a linkedlist in-place and return the new head."""
	# There's nothing to reverse
	if head is None or head.next is None:
		return head

	prev = None
	current = head
	# Iterate through the list and "reverse" each link
	while current is not None:
		next = current.next # Save forward path
		current.next = prev # Reverse link
		prev = current # Move prev forward
		current = next # Move current forward

	# Once 'current' reached None, 'prev' will point
	# to the last node
	return prev

def reverse_copy(head):
	"""Create a reversed *copy* of a linkedlist and
	return the new head.

	"""
	# There's nothing to reverse
	if head is None: return None

	current = head
	new = Node(head.value)
	# Iterate through the list and create new nodes
	# referring to the original list.
	while current.next is not None:
		next = Node(current.next.value, new) # Link backwards
		new = next # Move forward
		current = current.next

	# When current becomes None, new will point to the
	# last (aka the new head) node
	return new

if __name__ == "__main__":
	node = Node(1, Node(2, Node(3, Node(4)))) # 4 3 2 1
	node = Node(1) # 1
	node = Node(1, Node(2)) # 2 1
	node = reverse(node)
	while node is not None:
		#print node.value
		node = node.next

	node = Node(1, Node(2, Node(3, Node(4)))) # 4 3 2 1
	node = Node(1) # 1
	node = Node(1, Node(2)) # 2 1
	new_node = reverse_copy(node)
	while new_node is not None:
		print new_node.value
		new_node = new_node.next
	print "---"
	while node is not None:
		print node.value
		node = node.next
