def r_quick_sort(array, start, end):
	# Utility for swapping two elements of the array
	def swap(pos1, pos2):
		array[pos1], array[pos2] = array[pos2], array[pos1]

	if start >= end:
		return
	pivot = array[start]
	left = start+1
	right = end

	# Divide
	while left - right < 1:
		if array[left] > pivot:
			swap(left, right)
			right -= 1
		if array[left] <= pivot:
			left += 1

	# Insert pivot in its position
	swap(start, right)

	# Recurse
	r_quick_sort(array, start, right-1)
	r_quick_sort(array, left, end)

def quick_sort(array):
	r_quick_sort(array, 0, len(array)-1)

#################### DRIVERS ####################

l = [10, 1, 7, 3, 8, 9, 2, 6]
quick_sort(l)
print l
