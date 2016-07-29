"""This can actually be done by firstly reversing the two
sections separately, and then the whole array."""

def gcd(x, y):
	x, y = max(x, y), min(x, y)
	while y != 0:
		x, y = y, x%y
	return x

def rotate_array(arr, k):
	"""[1, 2, 3, 4, 5] with k=2 is [3, 4, 5, 1, 2]."""
	n = len(arr)

	# Utility for swapping elements
	def _swap(i, j):
		arr[i], arr[j] = arr[j], arr[i]

	iterations = gcd(n, k)
	for i in xrange(iterations):
		current = i
		for j in xrange(n/iterations - 1):
			next = (current + k) % n
			_swap(current, next)
			current = next

if __name__ == "__main__":
	arr = [1, 2, 3, 4, 5, 6, 7]
	k = 2
	rotate_array(arr, k)
	print arr

	arr = [1, 2, 3, 4, 5]
	k = 1
	rotate_array(arr, k)
	print arr

	arr = [1, 2, 3, 4, 5]
	k = 0
	rotate_array(arr, k)
	print arr

	arr = [1, 2, 3]
	k = 3
	rotate_array(arr, k)
	print arr

	arr = [1]
	k = 4
	rotate_array(arr, k)
	print arr

	arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
	k = 30 # Same effect as 6
	rotate_array(arr, k)
	print arr
