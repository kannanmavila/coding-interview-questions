class EmptyStack(Exception):
	pass

class Node:
	def __init__(self, value, next=None):
		self.value = value
		self.next = next


class Queue:
	def __init__(self, value=None):
		self.front = self.back = None
		if value is not None:
			self.front = self.back = Node(value)

	def enqueue(self, value):
		if self.front is None:
			self.front = self.back = Node(value)
			return
		self.back.next = Node(value)
		self.back = self.back.next
		return self

	def dequeue(self):
		if self.front is None:
			raise EmptyStack
		val = self.front.value
		self.front = self.front.next
		return val

if __name__ == "__main__":
	q = Queue(4)
	for i in [4, 8, 5, 9, 2, 5]:
		q.enqueue(i)
	while True:
		try:
			print q.dequeue()
		except EmptyStack:
			break
