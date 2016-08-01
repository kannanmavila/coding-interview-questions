def find_duplicate(array):
	start = 1
	end = len(array)-1
	while start != end:
		mid = (start + end) / 2
		lower_range = len([None for i in array if i >= start
				and i <= mid])

		if lower_range > mid - start + 1:
			# Go left
			end = mid
		else:
			# Go right
			start = mid + 1

	return start

if __name__ == "__main__":
	array = [1, 1, 3, 4, 5, 5, 6] # 5
	array = [1, 2, 2] # 2
	array = [1, 1] # 1
	print find_duplicate(array)
