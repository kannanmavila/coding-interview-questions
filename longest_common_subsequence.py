class InvalidParams(ValueError):
	pass


class LcsLookup(object):
	def __init__(self, x, y):
		n, m = len(x), len(y)
		self.lookup = [[None]*(m) for i in xrange(n)]

	def get(self, i, j):
		if -1 in (i, j):
			return 0
		return self.lookup[i][j]

	def set(self, i, j, value):
		try:
			self.lookup[i][j] = value
		except IndexError:
			raise InvalidParams(i, j)

	@property
	def result(self):
		return self.get(len(self.lookup)-1, len(self.lookup[0])-1)

def lcs(x, y):
	lookup = LcsLookup(x, y)
	for i in xrange(0, len(x)):
		for j in xrange(0, len(y)):
			if x[i] == y[j]:
				lookup.set(i, j, lookup.get(i-1, j-1) + 1)
			else:
				lookup.set(i, j, max(lookup.get(i, j-1),
						lookup.get(i-1, j)))
	return lookup.result

if __name__ == "__main__":
	x = "AGGTAB"
	y = "GXTXAYBZ"
	# Result: 4 ("GTAB")
	print lcs(x, y)
