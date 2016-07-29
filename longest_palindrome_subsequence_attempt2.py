class LPLookup(object):
	"""A lookup for longest-palindrome problem."""
	def __init__(self, n):
		self.table = [[None] * n for i in xrange(n)]

	def set(self, i, j, value):
		self.table[i][j] = value

	def get(self, i, j):
		if i == j:
			return 1
		if i > j:
			return 0
		return self.table[i][j]

	@property
	def result(self):
		n = len(self.table)
		return self.table[0][n-1]


def longest_palindrome(string):
	n = len(string)
	if n in (0, 1):
		return n
	lookup = LPLookup(n)

	for diff in xrange(1, n):
		for i in xrange(0, n-diff):
			j = i + diff
			if string[i] == string[j]:
				lookup.set(i, j, 2 + lookup.get(i+1, j-1))
			else:
				choices = [lookup.get(i+1, j),
						lookup.get(i, j-1)]
				lookup.set(i, j, max(choices))
	return lookup.result

if __name__ == "__main__":
	string = "BBABCBCAB" # 7 (BABCBAB)
	string = "A" # 1
	string = "" # 0
	string = "AB" # 1 (A or B)
	string = "GEEKSFORGEEKS" # 5
	print longest_palindrome(string)
