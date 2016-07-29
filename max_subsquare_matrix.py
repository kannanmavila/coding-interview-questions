class MaxSquareLookup(object):
	def __init__(self, array):
		n = len(array)
		m = len(array[0])
		self.table = [[0] * m for i in xrange(n)]

	def get(self, i, j):
		if i < 0 or j < 0:
			return 0
		return self.table[i][j]

	def set(self, i, j, value):
		self.table[i][j] = value

	@property
	def result(self):
		maxi = 0
		n = len(self.table)
		m = len(self.table[0])
		for i in xrange(n):
			for j in xrange(m):
				maxi = max(maxi, self.table[i][j])
		return maxi


def get_max_subsquare(array):
	n = len(array)
	if n == 0:
		return 0
	m = len(array[0])
	lookup = MaxSquareLookup(array)

	for i in xrange(n):
		for j in xrange(m):
			if array[i][j] == 0:
				lookup.set(i, j, 0)
			else:
				neighbors = [lookup.get(i, j-1),
						lookup.get(i-1, j),
						lookup.get(i-1, j-1)]
				lookup.set(i, j, 1 + min(neighbors))
	return lookup.result

if __name__ == "__main__":
	array = [
		[0, 1, 1, 0, 1],
		[1, 1, 0, 1, 0],
		[0, 1, 1, 1, 0],
		[1, 1, 1, 1, 0],
		[1, 1, 1, 1, 1],
		[0, 0, 0, 0, 0]]
	print get_max_subsquare(array) # 3

	array = [[1]]
	print get_max_subsquare(array) # 1

	array = [[]]
	print get_max_subsquare(array) # 0

	array = [
		[0, 1, 1, 0, 1],
		[1, 1, 0, 1, 0],
		[0, 1, 1, 0, 0],
		[1, 1, 1, 1, 0],
		[1, 1, 1, 1, 1],
		[0, 0, 0, 0, 0]]
	print get_max_subsquare(array) # 2
