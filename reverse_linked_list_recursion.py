class Node(object):
	def __init__(self, value, next=None):
		self.value = value
		self.next = next


def reverse(head):
	if head is None:
		return None
	head, tail = _reverse(head)
	tail.next = None
	return head

def _reverse(node):
	if node.next is None:
		return node, node

	head, tail = _reverse(node.next)
	tail.next = node
	return head, node

if __name__ == "__main__":
	head = Node(1, Node(2, Node(3, Node(4)))) # 4 3 2 1
	head = Node(10) # 10
	head = reverse(head)
	while head is not None:
		print head.value
		head = head.next
