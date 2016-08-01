def counting_sort(array, max_score):
	counts = [0] * (max_score + 1)

	for score in array:
		counts[score] += 1

	so_far = 0
	for i in xrange(max_score + 1):
		for j in xrange(so_far, so_far + counts[i]):
			array[j] = i
		so_far += counts[i]

if __name__ == "__main__":
	array = [1, 2, 3, 4, 2, 1, 6, 4]
	array = [1]
	array = []
	array = [5, 4, 3, 2, 1]
	array = [0, 0, 0]
	counting_sort(array, max(array + [0]))
	print array
