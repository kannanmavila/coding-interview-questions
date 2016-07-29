class Node(object):
	def __init__(self, value, next=None, prev=None, child=None):
		self.value = value
		self.next = next
		self.prev = prev
		self.child = child

def make_neighbors(a, b):
	a.next = b
	b.prev = a

def print_list(a):
	print "At: %s" % a.value
	if a.child is not None:
		print "Moving down from %s" % a.value
		print_list(a.child)
	if a.next is not None:
		print "Moving right from %s" % a.value
		print_list(a.next)

def flatten1(node):
	flat_child = flat_next = None
	if node.child is not None:
		flat_child = flatten(node.child)
		if node.next is not None:
			node.next.prev = flat_child
		flat_child.next = node.next
		node.next = node.child
		node.child = None
	if node.next is not None:
		flat_next = flatten(node.next)
	return flat_next or flat_child or node

def flatten2(head, tail):
	node = head
	while node is not None:
		if node.child is not None:
			make_neighbors(tail, node.child)
			tail = node.child
			while tail.next is not None:
				tail = tail.next
			#node.child = None
		node = node.next

def unflatten(node):
	while node is not None:
		if node.child is not None:
			node.child.prev.next = None
			node.child.prev = None
			unflatten(node.child)
		node = node.next

#################### DRIVERS ####################

five = Node(5)
tthree = Node(33)
two = Node(2)
one = Node(1)

six = Node(6)
tfive = Node(25)
eight = Node(8)
nine = Node(9)
seven = Node(7)

twelve = Node(12)

make_neighbors(five, tthree)
make_neighbors(tthree, two)
make_neighbors(two, one)
make_neighbors(six, tfive)
make_neighbors(eight, nine)

five.child = six
tfive.child = eight
nine.child = seven
two.child = twelve

#flatten1(five)
flatten2(five, one)
unflatten(five)
print_list(five)