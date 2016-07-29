def sorted_merge_with_gaps(arr1, arr2):
	"""Merge arr2 into arr1.

	arr1 and arr2 are sorted arrays, and arr1 contains enough
	gaps to accommodate all elements in arr2.

	"""
	m = len(arr1)
	n = len(arr2)

	if m == 0 or n == 0:
		return

	# Utility for swapping elements in arr1
	def _swap(left, right):
		arr1[left], arr1[right] = arr1[right], arr1[left]

	# Align gaps to the left of arr1
	right = m-1
	for i in xrange(m-1, -1, -1):
		if arr1[i] is not None:
			_swap(i, right)
			right -= 1

	# Utility for merging arr1 and arr2 into arr1
	def _merge(candidate, position, select_first=True):
		arr1[position] = arr1[candidate] if select_first \
				else arr2[candidate]
		return candidate+1

	# Merge arr2 and right portion of arr1 into
	# the gaps in arr1
	first = right + 1
	second = 0
	sorted_position = 0
	for i in xrange(m):
		if second == n: # Used up arr2
			first = _merge(first, sorted_position)
		elif first == m: # Used up arr1
			second = _merge(second, sorted_position, False)
		elif arr1[first] < arr2[second]:
			first = _merge(first, sorted_position)
		else:
			second = _merge(second, sorted_position, False)

		sorted_position += 1

if __name__ == "__main__":
	arr1 = [2, None, 7, None, None, 10, None]
	arr2 = [5, 8, 12, 14]
	sorted_merge_with_gaps(arr1, arr2)
	print arr1

	arr1 = [None]
	arr2 = [5]
	sorted_merge_with_gaps(arr1, arr2)
	print arr1

	arr1 = [2, None, 7, None, None, 10, None]
	arr2 = []
	sorted_merge_with_gaps(arr1, arr2)
	print arr1
