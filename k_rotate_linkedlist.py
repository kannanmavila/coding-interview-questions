class Node(object):
	def __init__(self, value, next=None):
		self.value = value
		self.next = next


class NotEnoughNodes(IndexError):
	pass


def rotate(head, k):
	# No rotation
	if k == 0:
		return head
	kth, next = None, head
	# Move k nodes forwards
	for i in xrange(k):
		try:
			kth, next = next, next.next
		except AttributeError:
			raise NotEnoughNodes(k)

	# There are only k nodes
	if next is None:
		return head

	# Find the last node
	last = next
	while last.next is not None:
		last = last.next

	# Rotate
	last.next = head
	head = next
	kth.next = None
	return head

def print_list(head):
	while head is not None:
		print head.value
		head = head.next
	print "--"

if __name__ == "__main__":
	head = Node(1, Node(2, Node(3, Node(4, Node(5)))))
	print_list(rotate(head, 3)) # 4 5 1 2 3
	head = Node(1, Node(2, Node(3, Node(4, Node(5)))))
	print_list(rotate(head, 5)) # 1 2 3 4 5
	head = Node(1, Node(2, Node(3, Node(4, Node(5)))))
	#print_list(rotate(head, 6)) # NotEnoughNodes: 6
	head = None
	#print_list(rotate(head, 1)) # NotEnoughNodes: 1
	print_list(rotate(head, 0)) # None
