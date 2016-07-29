class InvalidParams(ValueError):
	pass


class EmptyMatrix(ValueError):
	pass


class MinCostLookup(object):
	def __init__(self, costs):
		n, m = len(costs), len(costs[0])
		self.lookup = [[None]*(m) for i in xrange(n)]

	def get(self, i, j):
		if -1 in (i, j):
			return None
		return self.lookup[i][j]

	def set(self, i, j, value):
		try:
			self.lookup[i][j] = value
		except IndexError:
			raise InvalidParams(i, j)

	def result(self, i, j):
		return self.get(i, j)

def min_cost(costs, m, n):
	if not costs or not costs[0]:
		raise EmptyMatrix()
	if m < 0 or n < 0 or len(costs) < m+1 or len(costs[0]) < n+1:
		raise InvalidParams(m, n)
	lookup = MinCostLookup(costs)
	for i in xrange(0, m+1):
		for j in xrange(0, n+1):
			path_costs = [lookup.get(x, y)
					for x, y in [(i-1, j-1),
					(i-1, j), (i, j-1)]]
			path_costs = [cost for cost in path_costs
					if cost is not None]
			if not path_costs: path_costs = [0]
			best_cost = costs[i][j] + min(path_costs)
			lookup.set(i, j, best_cost)
	return lookup.result(m, n)

if __name__ == "__main__":
	costs = [
		[1, 2, 3],
		[4, 8, 2],
		[1, 5, 3]]
	print min_cost(costs, 3, 3)
