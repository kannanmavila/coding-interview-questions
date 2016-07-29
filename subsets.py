def print_subsets(super_set, index=0, subset=[]):
	if index == len(super_set):
		if subset:
			print "".join(map(str, subset))
		return
	subset.append(super_set[index])
	print_subsets(super_set, index+1, subset)
	subset.pop()
	print_subsets(super_set, index+1, subset)

def print_subsets_norecurse(super_set):
	set_size = len(super_set)
	def binary(i):
		result = bin(i)[2:]
		return "0"*(set_size - len(result)) + result

	for i in xrange(1, 2**set_size):
		subset = []
		rule = binary(i)
		for j in xrange(0, set_size):
			if rule[j] == '1':
				subset.append(super_set[j])
		print "".join(map(str, subset))

if __name__ == "__main__":
	print_subsets([1, 2, 3, 4])
	#print_subsets_norecurse([1, 2, 3, 4])
