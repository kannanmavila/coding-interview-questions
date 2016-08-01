class NoRotation(ValueError):
	pass


def rotation_point(array):
	left = 0
	right = len(array) - 1
	# left and right will never coincide. Hence,
	# we need to check when they're adjacent. When
	# this happens, the subarray of size will have
	# rotation in it, which means left will always
	# be greater than right. That means right is
	# always the answer.
	while right > left + 1:
		middle = (left + right) / 2
		if array[middle] > array[right]:
			left = middle # Move right
		else:
			right = middle # Move left

	# At this point, if left is smaller than right,
	# that means there is no rotation in the array
	if array[left] <= array[right]:
		raise NoRotation()
	return right

if __name__ == "__main__":
	array = [6, 7, 1, 2, 3, 4, 5]
	#array = [1] # NoRotation exception
	#array = [1, 2] # NoRotation exception
	print array[rotation_point(array)]
