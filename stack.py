class EmptyStack(Exception):
	pass


class Node:
	def __init__(self, value, next=None):
		self.value = value
		self.next = next


class Stack:
	def __init__(self, value=None):
		self.top = None
		if value is not None:
			self.top = Node(value)

	def pop(self, ):
		if self.top is None:
			raise EmptyStack
		val = self.top.value
		self.top = self.top.next
		return val

	def push(self, value):
		new_top = Node(value, self.top)
		self.top = new_top


if __name__ == "__main__":
	s = Stack(3)
	for i in [2, 4, 7, 4, 7]:
		s.push(i)
	while True:
		try:
			print s.pop()
		except EmptyStack:
			break
