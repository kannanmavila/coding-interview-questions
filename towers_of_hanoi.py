class Imbalance(Exception):
	pass


class EmptyTower(Exception):
	pass


class Disk:
	def __init__(self, value, next=None):
		self.value = value
		self.next = next


class Tower:
	def __init__(self, name):
		self.name = name
		self.head = None

	def push(self, value):
		if self.head is None:
			self.head = Disk(value)
			return

		# Balance condition
		if value > self.head.value:
			raise Imbalance("%s is greater than %s" \
				% (value, self.head.value))

		new_head = Node(value)
		new_head.next = self.head
		self.head = new_head

	def pop(self):
		if self.head is None:
			raise EmptyTower
		val = self.head.value
		self.head = self.head.next
		return val

	def move_top(self, tower):
		tower.push(self.pop())

	def move_many(self, dest, extra, n=None):
		# Abstraction
		if n == None:
			n = 0
			curr = self.head
			while curr is not None:
				n += 1
				curr = curr.next

		if (n > 0):
			self.move_many(extra, dest, n-1)
			self.move_top(dest)
			extra.move_many(dest, self, n-1)

def pop_print(tower):
	print "%s:" % tower.name
	while True:
		try:
			print tower.pop()
		except EmptyTower:
			return

if __name__ == "__main__":
	a = Tower("A")
	b = Tower("B")
	c = Tower("C")
	for i in xrange(10, 0, -1):
		a.push(i)
	a.move_many(c, b)
	pop_print(c)