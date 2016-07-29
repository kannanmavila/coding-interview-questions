class InvalidLookup(ValueError):
	pass


class LPSLookup(object):
	def __init__(self, string):
		n = len(string)
		self.lookup = [[None]*n for i in xrange(n)]

	def get(self, i, j):
		if i == j:
			return 1
		try:
			return self.lookup[i][j]
		except IndexError:
			raise InvalidLookup(i, j)

	def set(self, i, j, value):
		try:
			self.lookup[i][j] = value
		except IndexError:
			raise InvalidLookup(i, j)

	@property
	def result(self):
		return self.lookup[0][len(self.lookup)-1]


def longest_palindrome_subsequence(string):
	# TODO Check for edge cases
	lookup = LPSLookup(string)
	for j in xrange(1, len(string)):
		for i in xrange(j-1, -1, -1):
			print j, i
			if string[i] == string[j]:
				if j == i+1:
					lookup.set(i, j, 2)
				else:
					lookup.set(i, j,
						lookup.get(i+1, j-1) + 2)
			else:
				choices = [lookup.get(i, j-1),
						lookup.get(i+1, j)]
				lookup.set(i, j, max(choices))
	return lookup.result

if __name__ == "__main__":
	print longest_palindrome_subsequence("BBABCBCAB")
