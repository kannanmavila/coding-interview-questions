def max_sum(arr):
	"""Maximum sum using no two consecutive elements."""
	excluding = including = 0
	for i in arr:
		temp = including
		including = excluding + i
		excluding = max(temp, excluding)
	return max(including, excluding)

if __name__ == "__main__":
	arr = [3, 2, 7, 10]
	print max_sum(arr)
	arr = [3, 2, 5, 10, 7]
	print max_sum(arr)
