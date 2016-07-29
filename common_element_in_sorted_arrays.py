def common(arrays):
	"""Return the first common element in a set of sorted arrays."""
	n = len(arrays)
	if n == 0:
		return -1
	position = [0] * n
	max_array = 0

	# Utility to pick the next item to be considered in an array
	def next(i):
		return arrays[i][position[i]]

	while True:
		# Step 1: Increment all positions until the values
		# are greater than or equal to the one at current max_array
		for i in xrange(n):
			try:
				while next(i) < next(max_array):
					position[i] += 1
			except IndexError: # Ran out of elements
				return -1

			# Update max_array
			if next(i) > next(max_array):
				max_array = i

		# Step 2: Check if we found the common element
		if not [next(i) for i in xrange(n)
				if next(i) != next(max_array)]:
			break

	return next(max_array)

if __name__ == "__main__":
	arrays = [[1, 2, 3, 4, 5],
                    [2, 4, 5, 8, 10],
                    [3, 5, 7, 9, 11],
                    [1, 3, 5, 7, 9],
                  ] # 5
	arrays = [] # -1
	arrays = [[], [1, 2, 3]] # -1
	print common(arrays)
