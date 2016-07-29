class InvalidParams(ValueError):
	pass


class EditDistanceLookup(object):
	def __init__(self, x, y):
		n, m = len(x), len(y)
		self.lookup = [[None]*(m) for i in xrange(n)]

	def get(self, i, j):
		if -1 in (i, j):
			return max(i, j) + 1
		return self.lookup[i][j]

	def set(self, i, j, value):
		try:
			self.lookup[i][j] = value
		except IndexError:
			raise InvalidParams(i, j)

	@property
	def result(self):
		return self.get(len(self.lookup)-1, len(self.lookup[0])-1)

def edit_distance(x, y):
	lookup = EditDistanceLookup(x, y)
	for i in xrange(0, len(x)):
		for j in xrange(0, len(y)):
			if x[i] == y[j]: # No edit
				lookup.set(i, j, lookup.get(i-1, j-1))
			else:
				lookup.set(i, j, 1 + min(
						lookup.get(i-1, j),
						lookup.get(i, j-1),
						lookup.get(i-1, j-1)))
	return lookup.result

if __name__ == "__main__":
	x = "sunday"
	y = "saturday"
	print edit_distance(x, y)
