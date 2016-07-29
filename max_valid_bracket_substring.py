class Stack(object):
	def __init__(self):
		self.store = []

	def push(self, value):
		self.store.append(value)

	def pop(self):
		return self.store.pop()

	def empty(self):
		self.store = []

	@property
	def is_empty(self):
		return not self.store

	def size(self):
		return len(self.store)


def longest_valid_bracket_substring(string):
	"""Return the length of the longest valid bracket
	substring contained in `string`.

	"""
	# This stack will always contain the indices
	# that haven't been matched. Starts with -1,
	# meaning no unmatched indices.
	s = Stack()
	s.push(-1)
	max_streak = 0
	for i in xrange(len(string)):
		# Push the indices of open brackets
		if string[i] == "(":
			s.push(i)

		# Match the most recent open bracket
		# to this closing bracket, and pop the stack.
		# Now the top will have the last unmatched
		# index. Measure the distance and see if it
		# is greater than max_streak.
		else:
			# Matching bracket
			s.pop()

			# Invalid closing bracket; add to unmatched.
			# Note that at any point, we will store only
			# the most recent invalid closing bracket. In
			# the next iteration, if we encounter another
			# closing bracket, we'll remove this and insert
			# that.
			if s.is_empty:
				s.push(i)

			# Calculate the distance
			else:
				max_streak = max(max_streak,
						i - s.top())

	return max_streak

if __name__ == "__main__":
	strings = ["((()", # 2
		")()())", # 4
		"()(()))))", # 6
		")))))((((((((", # 0
		")()(", # 2
		"()((", # 2
		"(()(()", # 2
		"(((()((("] # 2
	for s in strings:
		#print longest_valid_bracket_substring(s)
		print findMaxLen(s)
