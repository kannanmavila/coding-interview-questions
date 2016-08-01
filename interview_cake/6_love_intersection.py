def intersection(a, b):
	"""Return the rectangle formed by the intersection
	of the two rectangles.

	Attributes:
		a - first rectangle
		b - second rectangle
		(Order doesn't matter)

	Raises:
		NoIntersection - If the two rectangle do not intersect

	"""
	# Left = max(a_left, b_left), Bottom = max(a_bottom, b_bottom)
	left_x = max(a['left_x'], b['left_x'])
	bottom_y = max(a['bottom_y'], b['bottom_y'])

	# Height = min(a_top, b_top) - max(a_bottom, b_bottom)
	height = min(a['bottom_y'] + a['height'],
			b['bottom_y'] + b['height']) - \
			bottom_y
	# Width = min(a_right, b_right) - max(a_left, b_left)
	width = min(a['left_x'] + a['width'],
			b['left_x'] + b['width']) - \
			left_x

	# Non-positive Height/Width ==> no intersection
	if height <= 0 or width <= 0:
		return None

	return {'left_x': left_x, 'bottom_y': bottom_y,
			'width': width, 'height': height}

if __name__ == "__main__":
	a = {'left_x': 1, 'bottom_y': 1,
			'width': 3, 'height': 2}
	b = {'left_x': 3, 'bottom_y': 0,
			'width': 1.5, 'height': 6}
	print intersection(a, b)
