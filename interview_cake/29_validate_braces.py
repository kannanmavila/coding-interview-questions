class Stack(object):
	def __init__(self):
		self.container = []

	def put(self, value):
		self.container.append(value)

	def pop(self):
		return self.container.pop()

	def peek(self):
		n = len(self.container)
		return self.container[n-1]

	def is_empty(self):
		return len(self.container) == 0


def validate_braces(string):
	stack = Stack()
	openers = ['(', '{', '[']
	closers = [')', '}', ']']
	compliment = {closers[i]: openers[i]
			for i in xrange(3)}
	
	for c in string:
		if c in openers:
			stack.put(c)

		elif c in closers:
			try:
				if stack.peek() == compliment[c]:
					stack.pop()
				else:
					return False
			except IndexError:
				return False

	return stack.is_empty()

if __name__ == "__main__":
	string = "{ [ ] ( ) }" # True
	string = "{ [ ( ] ) }" # False
	string = "{ [ }"
	string = ""
	string = "{"
	string = "}"
	print validate_braces(string)
