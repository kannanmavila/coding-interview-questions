def change_choices(n, denominations):
	# No. of ways to make zero is one - by choosing nothing.
	table = [1] + [0] * n

	# For every denomination Di, update the table for
	# all values greater than or equal to Di. Since this
	# in done incrementally, it takes care of multiple
	# uses of Di. Since this is done per denomination,
	# different permutations of the same choice won't
	# be counted again.
	for d in denominations:
		for i in xrange(d, n+1): # Assumption: d is +ve
			table[i] += table[i-d]
	return table[n]

if __name__ == "__main__":
	ways = change_choices(3, [5, 2, 3, 1]) # 3
	print "ways:", ways
