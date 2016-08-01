class Product(object):
	def __init__(self, array):
		n = len(array)
		self.left = [None] * n
		self.right = [None] * n
		# Iterate from each side and fill in
		# lookup table with product till 'i'
		left_prod = 1
		right_prod = 1
		for i in xrange(n):
			left_prod *= array[i]
			right_prod *= array[n-i-1]
			self.left[i] = left_prod
			self.right[n-i-1] = right_prod

	def get_left(self, i):
		# Out of bounds
		if i < 0 or i >= len(self.left): return 1

		return self.left[i]

	def get_right(self, i):
		# Out of bounds
		if i < 0 or i >= len(self.right): return 1

		return self.right[i]


def get_products_of_all_ints_except_at_index(array):
	product = Product(array)
	result = []
	# For every position, multiple left lookup
	# with right lookup
	for i in xrange(len(array)):
		this = product.get_left(i-1) * product.get_right(i+1)
		result.append(this)
	return result

print get_products_of_all_ints_except_at_index([1, 2, 6, 0, 9])
