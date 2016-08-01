def highest_product(array):
	"""Return the maximum product that can be produced using
	three integers from 'array'.

	"""
	max1 = max2 = max3 = None
	min1 = min2 = float('inf')
	for num in array:
		# "Trickle in" num among maximums
		if num > max3: max3 = num
		if num > max2:
			max2, max3 = max3, max2
		if num > max1:
			max1, max2 = max2, max1

		# "Trickle in" num among minimums
		if num < min2:
			min2 = num
		if num < min1:
			min1, min2 = min2, min1

	# Possibility 1: + + +
	# Possibility 2: - - +
	return max(max1 * max2 * max3, max1 * min1 * min2)

print highest_product([-10, -10, 1, 3, 2]) # 300
print highest_product([1, 10, -5, 1, -100]) # 5000
print highest_product([1, 2, 3, 4, 5, -100, -1]) # 500
print highest_product([-1, -2, -3]) # -6
