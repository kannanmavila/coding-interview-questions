def merge_lists(my_list, alices_list):
	"""A 2-way merge."""
	p1 = p2 = 0 # Pointers
	l1 = len(my_list)
	l2 = len(alices_list)
	result = [None] * (l1 + l2)

	# Merge
	for i in xrange(l1 + l2):
		mine = my_list[p1] if p1 < l1 \
				else float('inf')
		alices = alices_list[p2] if p2 < l2 \
				else float('inf')
		if mine < alices:
			p1 += 1
			result[i] = mine
		else:
			p2 += 1
			result[i] = alices
	return result


class Heap(object):
	"""A heap mimicry using list."""
	def __init__(self):
		self.container = []

	def push(self, value):
		self.container.append(value)
		self.container.sort()

	def pop(self):
		return self.container.pop(0)


def merge_k_lists(*lists):
	"""A k-way merge of sorted lists."""
	N = sum([len(list) for list in lists])
	result = [None] * N
	pointer = [0] * len(lists) # a pointer for each list

	# Create heap
	heap = Heap()
	for l in xrange(len(lists)):
		try:
			heap.push((lists[l][0], l))
		except IndexError:
			pass

	# Merge
	for i in xrange(N):
		(result[i], min_list) = heap.pop()
		pointer[min_list] += 1
		try:
			heap.push((lists[min_list][pointer[min_list]],
					min_list))
		except IndexError:
			pass

	return result


class Node(object):
	def __init__(self, value, next=None):
		self.value = value
		self.next = next

def merge_linked_lists(l1, l2):
	head = None
	INF = float('inf')

	while l1 is not None or l2 is not None:
		min_list = min(
			(l1.value if l1 is not None else INF, l1),
			(l2.value if l2 is not None else INF, l2))[1]

		# First iteration
		if head is None:
			head = prev = min_list
		# Subsequent iterations
		else:
			prev.next = min_list # Connect to previous
			prev = prev.next # Progress prev pointer

		# Progress the pointer that provided min value
		if l1 == min_list:
			l1 = l1.next
		else:
			l2 = l2.next
	return head

if __name__ == "__main__":
	# merge_lists
	my_list = [1, 2, 9]
	alices_list = [0, 1, 1, 5, 10]
	print merge_lists(my_list, alices_list)

	# k-way merge
	lists = [[1, 3, 6],
		[3, 7, 8],
		[10]]
	lists = [[1, 2, 3], [], []]
	print merge_k_lists(*lists)

	# merge_linked_lists
	l1 = Node(1, Node(2, Node(4)))
	l2 = Node(3, Node(5, Node(5, Node(6))))
	res = merge_linked_lists(l1, l2)
	while res is not None:
		print res.value
		res = res.next
