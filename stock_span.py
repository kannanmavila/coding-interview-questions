class Stack(object):
	def __init__(self):
		self.store = []

	def push(self, value):
		self.store.append(value)

	def top(self):
		return self.store[len(self.store) - 1]

	def pop(self):
		return self.store.pop()

	def is_empty(self):
		return not self.store


def print_stock_span(array):
	"""Print the stock span of every day in `array`.

	Stock span of day Di is defined as the number of
	consecutive days before Di that had a stock value
	less than or equal to that of Di.

	"""
	# This stack stores (stock_value, span) pairs for days
	stack = Stack()
	for i in array:
		span = 1
		while not stack.is_empty() and \
				stack.top()[0] < i:
			span += stack.pop()[1]
		stack.push((i, span))
		print span

if __name__ == "__main__":
	array = [10, 4, 5, 90, 120, 80] # 1 1 2 4 5 1
	array = [100, 80, 60, 70, 60, 75, 85] # 1 1 1 2 1 4 6
	print_stock_span(array)
