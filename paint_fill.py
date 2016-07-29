from time import sleep
class NoSuchPoint(Exception):
	pass


class Point(object):
	"""A 2-d point on the screen."""
	def __init__(self, x , y):
		self.x = x
		self.y = y

	def get_neighbors(self):
		neighbors = [Point(self.x+1, self.y), # South
			Point(self.x-1, self.y), # North
			Point(self.x, self.y+1), # East
			Point(self.x, self.y-1), # West
			Point(self.x+1, self.y+1), # SE
			Point(self.x+1, self.y-1), # SW
			Point(self.x-1, self.y+1), # NE
			Point(self.x-1, self.y-1)] # NW
		return [n for n in neighbors if n.x >= 0 and n.y >= 0]

	def __repr__(self):
		return "(%s, %s)" % (self.x, self.y)


class Color(object):
	"""A color for a point.

	Attributes:
		value: The value for the color. 0x0 by default

	"""
	def __init__(self, value=0x0):
		self.value = value

	def __repr__(self):
		return str(self.value)

	def __cmp__(self, other):
		return cmp(self.value, other.value)


class Screen(object):
	"""A 2-d display screen.

	Attributes:
		x: the length of the x-axis
		y: the length of the y-axis
		default_color: default color to fill the screen with

	"""
	def __init__(self, x, y, default_color=None):
		self.grid = [[default_color for j in xrange(y)]
				for i in xrange(x)]

	@classmethod
	def from_matrix(cls, matrix):
		"""Create a Screen from a matrix of values for colors.

		Args:
			matrix: the matrix containing the color values

		Returns:
			screen: A Screen containing colors initialized to
				the values in `matrix`

		"""
		screen = cls(len(matrix), len(matrix[0]))
		for i in xrange(0, len(matrix)):
			for j in xrange(0, len(matrix[i])):
				screen.color(Point(i, j),
					Color(matrix[i][j]))
		return screen

	def color(self, point, color):
		"""Color a point with a specified color.

		Args:
			point: point to be colored
			color: color to paint `point` with

		Returns:
			None

		Raises:
			NoSuchPoint: The point does not exist within
				the screen

		"""
		try:
			self.grid[point.x][point.y] = color
		except IndexError:
			raise NoSuchPoint(point)

	def get_color(self, point):
		"""Return the color of a point

		Args:
			point: the point

		Raises:
			NoSuchPoint: `point` does not exist within
				the screen

		"""
		try:
			return self.grid[point.x][point.y]
		except IndexError:
			raise NoSuchPoint(point)

	def paint_fill(self, point, color):
		"""Do a bucket-fill, starting at `point`

		Starting from `point`, perform a bucket-fill with `color`,
		to all connected points on the screen.

		Args:
			point: the point to start at
			color: the color to use

		"""
		try:
			# Color if point exists
			original_color = self.get_color(point)
			self.color(point, color)
		except NoSuchPoint:
			return

		# Recurse to neighbors with the same color
		for n in point.get_neighbors():
			try:
				if self.get_color(n) == original_color:
					self.paint_fill(n, color)
			except NoSuchPoint:
				pass

if __name__ == "__main__":
	matrix = \
	       [[0, 0, 0, 0, 0],
		[0, 0, 1, 1, 1],
		[0, 1, 1, 1, 1],
		[1, 0, 1, 1, 1],
		[0, 1, 0, 0, 0],
		[0, 0, 1, 1, 1],
		[0, 0, 1, 1, 1],
		[0, 0, 1, 0, 0]]
	screen = Screen.from_matrix(matrix)
	screen.paint_fill(Point(1, 2), Color('X'))
	for g in screen.grid:
		print g
