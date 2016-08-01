def get_products_of_all_ints_except_at_index(array):
	# If there are more than one zero, then
	# the result will contain all zeroes
	zeros = 0
	for num in array:
		if num == 0: zeros += 1
	if zeros > 1: return [0] * len(array)

	product = 1
	for num in array:
		product *= max(num, 1) # Ignore zero

	# (1-zeros) trick: If there is a zero, result will
	# contain all but one zeroes.
	return [product*(1-zeros)/num if num != 0 else product
			for num in array]

print get_products_of_all_ints_except_at_index([1, 2, 6, 5, 9])
