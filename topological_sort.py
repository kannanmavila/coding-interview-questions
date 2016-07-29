def topological_sort(dag):
	n = len(dag)
	visited = [False] * n
	order = []

	# Utility method for DFS
	def _trace(i):
		if visited[i]:
			return

		visited[i] = True
		for j in xrange(n):
			if dag[i][j] != 0: # Edge exists
				_trace(j)
		order.append(i)

	# Start from each node
	for i in xrange(n):
		_trace(i)

	# Finally, reverse the order (that's just how it works)
	return order[::-1]

if __name__ == "__main__":
	dag = [
		[0, 1, 0, 0, 0, 1],
		[0, 0, 1, 1, 1, 0],
		[0, 0, 0, 1, 1, 0],
		[0, 0, 0, 0, 1, 0],
		[0, 0, 0, 0, 0, 0],
		[0, 1, 1, 0, 0, 0]] # 0 5 1 2 3 4
	dag = [
		[0] * 6, # No outgoing edge
		[0] * 6, # No outgoing edge
		[0, 0, 0, 1, 0, 0],
		[0, 1, 0, 0, 0, 0],
		[1, 1, 0, 0, 0, 0],
		[1, 0, 1, 0, 0, 0]] # 5 4 2 3 1 0
	dag = [[1]] # 0
	dag = [[0]] # 0
	dag = [] # []
	print topological_sort(dag)
