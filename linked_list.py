class NodeNotFound(Exception):
	pass

class NotEnoughNodes(Exception):
	pass

class Node:
	def __init__(self, value, next=None):
		self.value = value
		self.next = next

	def print_list(self):
		curr = self
		while curr is not None:
			print curr.value
			curr = curr.next
		print ""

	def add_to_tail(self, *values):
		curr = self
		while curr.next is not None:
			curr = curr.next

		for v in values:
			curr.next = Node(v)
			curr = curr.next
		return self

	def delete(self, value): # Cannot delete head
		curr = self
		while curr.next is not None:
			if curr.next.value == value:
				curr.next = curr.next.next
				return
			curr = curr.next
		raise NodeNotFound(value)

	def has_loop(self):
		p1 = p2 = self
		while True:
			try:
				p1 = p1.next
				p2 = p2.next.next
			except AttributeError:
				return False
			if p1 == p2:
				return True

	def dedup(self):
		i = self
		while i.next is not None:
			prev = i
			j = i.next
			while j is not None:
				# Delete j
				if i.value == j.value:
					prev.next = j = j.next
				else:
					prev , j = j, j.next
			i = i.next

	def nth_from_end(self, n):
		p1 = p2 = self
		for i in xrange(n+1):
			try:
				p2 = p2.next
			except AttributeError:
				raise NotEnoughNodes("%d needed" % (n+1))
		while p2 is not None:
			p1 = p1.next
			p2 = p2.next
		return p1.value

def delete_by_reference(node):
	if node is None or node.next is None:
		raise NodeNotFound
	node.value = node.next.value
	node.next = node.next.next

#################### DRIVERS ####################

if __name__ == "__main__":
	n = Node(1).add_to_tail(2, 1, 2, 2, 3, 4, 5, 3)
	n.dedup()
	#print n.nth_from_end(4)
	delete_by_reference(n.next)
	n.print_list()
