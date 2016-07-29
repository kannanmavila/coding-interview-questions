class Queue(object):
	def __init__(self):
		self.store = []

	def push(self, *values):
		self.store.append(values)

	def pop(self):
		return self.store.pop(0)

	def is_empty(self):
		return not self.store


def time_to_rot(matrix):
	"""Return the number of units of time required to rot
	all fresh oranges in the matrix. '2' represents rotten
	oranges, '1' fresh, and '0' empty cells. A rotten orange
	can rot neighboring four (exluding diagonal neighbors)
	oranges in a single unit of time. Return None if all
	oranges cannot be rotten.

	"""
	n = len(matrix)
	if n == 0: return 0
	m = len(matrix[0])

	# Create a queue and add all rotten oranges to it.
	rotten = Queue()
	for i in xrange(n):
		for j in xrange(m):
			if matrix[i][j] == 2:
				rotten.push(i, j, 0) # i, j, time-to-rot

	# Perform BFS on matrix and progressively rot neighboring
	# oranges, keeping track of time.
	visited = [[False] * m for i in xrange(n)]
	time = 0 # Big bang!
	while not rotten.is_empty():
		i, j, time = rotten.pop()
		neighbors = [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]
		for i, j in neighbors:
			# Out of bounds
			if i < 0 or j < 0 or i == n or j == m:
				continue

			if matrix[i][j] == 1 and \
					not visited[i][j]:
				visited[i][j] = True
				rotten.push(i, j, time+1)

	# Check for fresh oranges.
	for i in xrange(n):
		for j in xrange(m):
			if matrix[i][j] == 1 and not visited[i][j]:
				return None

	return time

if __name__ == "__main__":
	matrix = [[2, 1, 0, 2, 1],
		  [1, 0, 1, 2, 1],
		  [1, 0, 0, 2, 1]]
	print time_to_rot(matrix)
