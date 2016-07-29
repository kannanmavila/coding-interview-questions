class InvalidPosition(ValueError):
	pass


class EmptyHeap(ValueError):
	pass


class MinHeap(object):
	def __init__(self, values=[]):
		self.values = []
		self._heapify(values)

	def _heapify(self, values):
		self.values = values
		for i in xrange(self.length/2, self.length):
			self._trickle_up(i)

	@property
	def length(self):
		return len(self.values)

	def add(self, value):
		self.values.append(value)
		self._trickle_up(self.length-1)

	def _swap(self, i, j):
		self.values[i], self.values[j] = \
				self.values[j], self.values[i]

	def _trickle_up(self, i):
		if i == 0:
			return
		parent = (i+1)/2 - 1
		try:
			if self.values[parent] > self.values[i]:
				self._swap(parent, i)
			self._trickle_up(parent)
		except IndexError:
			raise InvalidPosition(i)

	def peek(self):
		try:
			return self.values[0]
		except IndexError:
			raise EmptyHeap()

	def pop(self):
		value = self.peek()
		try:
			self.values[0] = self.values.pop()
		except IndexError: # Popping the only element
			return value
		self._trickle_down(0)
		return value

	def _trickle_down(self, i):
		children = [2*i + 1, 2*i + 2]
		for child in children:
			try:
				# Possibly for both
				if self.values[child] < self.values[i]:
					self._swap(child, i)
				self._trickle_down(child)
			except IndexError:
				pass

if __name__ == "__main__":
	heap = MinHeap([4, 9, 11, 6, 5, 20, 2, 3, 7])
	heap.add(8)
	while True:
		print heap.values
		try:
			heap.pop()
		except EmptyHeap:
			break
