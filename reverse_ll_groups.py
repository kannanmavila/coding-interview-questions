class Node(object):
	def __init__(self, value, next=None):
		self.value = value
		self.next = next


def reverse(head, k):
	"""Reverse the linkedlist beginning at `head`, `k` nodes
	at a time. e.g. 1->2->3->4->5->6->7->8 with a k value of
	3 will become 3->2->1->6->5->4->8->7.

	"""
	# Empty list
	if head is None:
		return None

	# Iteratively reverse k nodes at a time
	counter = 0
	current, next = head, head.next
	while counter < k-1: # reverse k-1 links
		# List size less than k
		if next is None:
			head.next = None
			return current

		# Save for next step
		later = next.next

		# Reverse link
		next.next = current
		counter += 1

		# Move forward
		current, next = next, later

	# Link the head to the head of the next reversed sublist
	head.next = reverse(next, k)

	# Return the new head (old tail) so that it can be connected
	# to previous sublists if any
	return current

def repr(node):
	if node is None:
		return "X"
	return str(node.value) + " -> " + repr(node.next)

if __name__ == "__main__":
	head = Node(1, Node(2, Node(3, Node(4, Node(5, Node(6,
			Node(7, Node(8))))))))
	print repr(reverse(head, 3))

	head = Node(1, Node(2))
	print repr(reverse(head, 1))