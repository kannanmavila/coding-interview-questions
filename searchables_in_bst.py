def count_searchable(array):
	return _count_searchable(array, 0, len(array)-1,
			-float('inf'), float('inf'))

def _count_searchable(array, left, right, min, max):
	if left > right:
		return 0

	mid = (left + right) / 2

	current = 0
	if min < array[mid] < max:
		current = 1
		print array[mid]
	return current + _count_searchable(array, left, mid-1,
					min, array[mid]) + \
			_count_searchable(array, mid+1, right,
					array[mid], max)

if __name__ == "__main__":
	array = [1, 3, 7, 2, 4, 6] # 4
	array = [9, 1, 2, 5, 3, 7] # 3
	array = [1] # 1
	array = [] # 0
	array = [1, 2, 3, 4, 5] # 5
	array = [5, 4, 3, 2, 1] # 1
	print count_searchable(array), "searchable(s)"
