class UniqueNotFound(ValueError):
	pass


def get_unique(array):
	"""Return the one integer in 'array' that is unique.

	NB: Will no work if there are multiple values that
	appear odd number of times.

	"""
	unique = 0
	for id in array:
		unique ^= id

	# Since id is positive, unique == 0 would mean
	# there is no unique id in the array
	if unique == 0:
		raise UniqueNotFound()
	return unique

if __name__ == "__main__":
	array = [1, 1, 2, 3, 4, 2, 4]
	print get_unique(array)
