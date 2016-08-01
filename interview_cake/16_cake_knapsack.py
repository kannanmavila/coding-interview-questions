def max_duffel_bag_value(cakes, capacity):
	"""Return the maximum value of cakes that can be
	fit into a bag. There are infinitely many number
	of each type of cake.

	Caveats:
		1. Capacity can be zero (naturally handled)
		2. Weights can be zero (checked at the start)
		3. A zero-weight cake can give infinite value
			iff its value is non-zero

	Attributes:
		cakes - list of cakes represented by a
			(weight, value) tuple
		capacity - the maximum weight the bag can carry

	"""
	# If there is a cake with zero weight and non-zero
	# value, the result is infinity.
	if [c for c in cakes if c[0] == 0 and c[1] > 0]:
		return float('inf')
	max_value = [0] * (capacity+1)
	for i in xrange(1, capacity+1):
		# For every cake that weighs not more
		# than i, see if including it will
		# give better results for capacity 'i'
		choices = [max_value[i-cake[0]] + cake[1]
				for cake in cakes
				if cake[0] <= i] + [0]
		max_value[i] = max(choices)
	return max_value[capacity]

if __name__ == "__main__":
	cakes = [(7, 160), (3, 90), (2, 15)]
	print max_duffel_bag_value(cakes, 20) # 555 (6*90 + 1*15)
