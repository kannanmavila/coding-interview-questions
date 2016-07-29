class Stack(object):
	def __init__(self):
		self.store = []

	def push(self, *values):
		for v in values:
			self.store.append(v)

	def pop(self):
		return self.store.pop()

	def top(self):
		return self.store[len(self.store)-1]

	def is_empty(self):
		return not self.store

	def flush(self):
		while self.store:
			print self.store.pop()


def sorted_insert(stack, value):
	"""Insert `value` into the already sorted `stack`, at
	the proper position.

	"""
	# Found the location, or the stack is empty
	if stack.is_empty() or stack.top() <= value:
		stack.push(value)
		return

	# Found a greater element that needs to be stored
	# in this recursion stack and put back once `value`
	# has been inserted.
	temp = stack.pop()
	sorted_insert(stack, value)
	stack.push(temp)

def sort(stack):
	"""Sort a stack, using recursion."""
	# Nothing to sort
	if stack.is_empty(): return

	# Pop every element, sort the rest of the stack,
	# and insert the element in its sorted order.
	temp = stack.pop()
	sort(stack)
	sorted_insert(stack, temp)

if __name__ == "__main__":
	stack = Stack()
	stack.push(-3, 14, 18, -5, 30)
	sort(stack)
	stack.flush()
