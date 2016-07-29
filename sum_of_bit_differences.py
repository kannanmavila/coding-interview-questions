def bit_difference(array):
	"""Return the sum of bit differences of all possible pairs
	in array. (x, y) and (y, x) are different pairs.

	Bit difference of two numbers are the number of positions
	at which their bits differ.

	"""
	total = 0
	n = len(array)
	for i in xrange(32):
		count = sum([1 for num in array
				if (1<<i)&num > 0])

		# With count number of '1' bits,
		# count * (n - count) number of pairs
		# with bit difference can be created.
		# Multiply by two because (x, y) and (y, x)
		# are considered different pairs.
		total += count * (n-count) * 2
	return total

if __name__ == "__main__":
	array = [1, 3, 5]
	print bit_difference(array)
