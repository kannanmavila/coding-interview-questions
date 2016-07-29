"""THIS DOESN'T WORK!!!"""

EPSILON = 0.0001


class Point(object):
	"""A 2-d point.

	Attributes:
		x: x value
		y: y value

	"""
	def __init__(self, x, y):
		self.x = x
		self.y = y

	def __repr__(self):
		return "(%s, %s)" % (self.x, self.y)


class Line(object):
	"""A line on the 2-d plane.

	Attributes:
		slope: the slope of the line
		y_intercept: the intercept on y-axis

	"""
	def __init__(self, p1, p2):
		self.points = []
		if p2.x == p1.x: # Infinite slope
			self.slope = self.y_intercept = None
		else:
			self.slope = float(p2.y - p1.y) / (p2.x - p1.x)
			self.y_intercept = p1.y - p1.x * self.slope

	def __eq__(self, other):
		if (self.slope, other.slope) == (None, None):
			return True
		if None in (self.slope, other.slope):
			return False
		return abs(self.slope - other.slope) < EPSILON

	def __repr__(self):
		return "Slope: %s, y-intercept: %s" % (self.slope,
				self.y_intercept)

class PointLine(Line):
	"""A line that can keep track of points on them."""
	def __init__(self, p1, p2):
		Line.__init__(self, p1, p2)
		self.points = [p1, p2]

	def add_point(self, point):
		self.points.append(point)

	@property
	def count(self):
		return len(self.points)


def get_max_line(points):
	max_line = None
	for i in xrange(0, len(points)-1):
		point = points[i]
		line = None
		for j in xrange(i+1, len(points)):
			other = points[j]
			if line is None: # First "other" point
				line = PointLine(point, other)
				continue
			if line == Line(point, other):
				line.add_point(other)
		if max_line is None or line.count > max_line.count:
			max_line = line
	return max_line

if __name__ == "__main__":
	points = [(0, 0), (3, 2), (3, 4), (4, 4), (3, 1), (3, 100),
			(2, 4)]
	points = [(1, 1), (1, 2), (2, 2), (2, 1), (3, 3)]
	points = [Point(p[0], p[1]) for p in points]
	max_line = get_max_line(points)
	print max_line.count
