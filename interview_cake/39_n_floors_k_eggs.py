def min_drops(floors, eggs):
	drops = [[None] * (eggs + 1) for i in xrange(floors+1)]

	# With zero eggs, it's impossible.
	# Note that zeroth floor is an exception, and
	# will be rewritten in the next step.
	for i in xrange(floors+1):
		drops[i][0] = float('inf')

	# No drops required if there are no floors
	for i in xrange(eggs+1):
		drops[0][i] = 0

	# Memoize, and iteratively build-up
	for f in xrange(1, floors+1):
		for e in xrange(1, eggs+1):
			# Try dropping from every floor
			choices = [1 + max(drops[i-1][e-1], drops[f-i][e])
					for i in xrange(1, f+1)]
			# Best choice
			drops[f][e] = min(choices)
	return drops[floors][eggs]

if __name__ == "__main__":
	print min_drops(100, 2) # 14
	print min_drops(10, 2) # 4
	print min_drops(10, 200) # 4
	print min_drops(1, 1) # 1
	print min_drops(1, 0) # inf
	print min_drops(0, 2) # 0
