def spiral_print(matrix):
	polarity = 1
	n = len(matrix)-1
	m = len(matrix[0])
	x, y = 0, -1
	while True:
		if m == 0:
			return
		# Go right/left
		for i in xrange(m):
			y += polarity
			print matrix[x][y]
		m -= 1
		if n == 0:
			return
		# Go up/down
		for i in xrange(n):
			x += polarity
			print matrix[x][y]
		n -= 1
		polarity = -polarity

if __name__ == "__main__":
	matrix1 = \
	       [[1, 2, 4, 3],
		[9, 4, 7, 0],
		[2, 5, 2, -5],
		[3, 3, 3, 3]]
	matrix2 = \
	       [[1],
		[1],
		[1]]
	matrix3 = \
	       [[1, 1, 1]]
	matrix4 = \
	       [[1]]
	spiral_print(matrix3)
