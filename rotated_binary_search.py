class ItemNotFound(Exception):
	pass


debug = False
def find_min(array):
	left = 0
	right = len(array)-1
	while True:
		if left >= right-1:
			return right

		middle = (left + right + 1) / 2
		if debug:
			print "left: %d, middle: %d, right: %d" \
				% (array[left], array[middle], array[right])
		if array[left] < array[middle]:
			left = middle
		else:
			right = middle

def rotated_binary_search(array, value):
	left = 0
	right = len(array)-1
	while True:
		mid = (right + left) / 2
		# Found!
		if array[mid] == value:
			return mid

		# Not found :(
		if left == right:
			raise ItemNotFound(value)

		# Case 1: Pivot in right subset
		if array[mid] >= array[left]:
			if array[left] <= value < array[mid]:
				right = mid - 1
			else:
				left = mid + 1

		# Case 2: Pivot in left subset
		else:
			if array[mid] < value <= array[right]:
				left = mid + 1
			else:
				right = mid - 1

if __name__ == "__main__":
	l = [15, 16, 19, 20, 25, 1, 3, 4, 5, 7, 10, 14]
	#print find_min(l)
	for i in l:
		print rotated_binary_search(l, i)
