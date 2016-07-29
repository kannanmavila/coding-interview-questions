class EmptyStack(Exception):
	pass


class Node:
	def __init__(self, value, next=None):
		self.value = value
		self.next = next


class Stack:
	def __init__(self, head=None):
		self.head = Node(head) if head is not None else None

	def push(self, *values):
		for v in values:
			new_head = Node(v, self.head)
			self.head = new_head
		return self

	def pop(self):
		if self.head is None:
			raise EmptyStack
		val = self.head.value
		self.head = self.head.next
		return val

	def is_empty(self):
		return self.head is None

	def peek(self):
		if self.head is None:
			raise EmptyStack
		return self.head.value

	def sort(self):
		sorted = Stack()
		while not self.is_empty():
			curr = self.pop()
			while not sorted.is_empty() \
				and sorted.peek() < curr:
				self.push(sorted.pop())
			sorted.push(curr)
		self.head = sorted.head


if __name__ == "__main__":
	s = Stack().push(1, 2, 3, 2, 4, 5, 1)
	s.sort()
	while True:
		try:
			print s.pop()
		except EmptyStack:
			break
