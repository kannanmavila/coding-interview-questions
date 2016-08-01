MAX_TEMP = 110


class NoData(IndexError):
	"""No data has been recorded."""
	pass


class InvalidTemperature(ValueError):
	"""Temparatures range from 0 to 110."""
	pass


class TempTracker:
	"""Tracks various metrics related to temparature readings."""
	def __init__(self):
		self.min = float('inf') # Arbitrarily large
		self.max = None # Arbitrarity small
		self.mean = float(0) # Real number
		self.count = 0
		self.counter = [0] * (MAX_TEMP + 1)

	def insert(self, value):
		if value < 0 or value > 110:
			raise InvalidTemperature()
		self.max = max(value, self.max)
		self.min = min(value, self.min)
		self.mean = (self.count * self.mean + value) \
				/ (self.count + 1)
		
		# Update overall count
		self.count += 1
		# Update counter for 'value'
		self.counter[value] += 1

	def get_max(self):
		if self.max is None:
			raise NoData()
		return self.max

	def get_min(self):
		if self.min == float('inf'):
			raise NoData()
		return self.min

	def get_mean(self):
		if self.max is None:
			raise NoData()
		return self.mean

	def get_mode(self):
		if self.max is None:
			raise NoData()
		return self.counter.index(max(self.counter))


if __name__ == "__main__":
	t = TempTracker()
	#print t.get_mode() # NoData exception
	t.insert(3)
	print t.get_max(), t.get_min(), t.get_mean(), t.get_mode()
	t.insert(5)
	t.insert(5)
	#t.insert(1110) # InvalidTemparature exception
	print t.get_max(), t.get_min(), t.get_mean(), t.get_mode()
