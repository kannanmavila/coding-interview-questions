class EmptyStack(Exception):
	pass


class EmptyQueue(EmptyStack):
	pass


class Node:
	def __init__(self, value, next=None):
		self.value = value
		self.next = next


class Stack:
	def __init__(self, head=None):
		self.head = Node(head) if head is not None else None

	def pop(self):
		if self.head is None:
			raise EmptyStack()
		val = self.head.value
		self.head = self.head.next
		return val

	def push(self, *values):
		for v in values:
			new_head = Node(v, self.head)
			self.head = new_head


class Queue:
	def __init__(self, front=None):
		self.push_stack = Stack()
		self.pop_stack = Stack(front)

	def push(self, *values):
		self.push_stack.push(*values)
		return self

	def pop(self):
		try:
			return self.pop_stack.pop()
		except EmptyStack:
			while True:
				try:
					self.pop_stack.push(
						self.push_stack.pop())
					print "Transferring..."
				except EmptyStack:
					break
		try:
			return self.pop_stack.pop()
		except EmptyStack:
			raise EmptyQueue()


if __name__ == "__main__":
	q = Queue().push(1, 2, 3, 4, 5)
	for i in xrange(3):
		print q.pop()
	q.push(6, 7, 8)
	while True:
		print q.pop()
