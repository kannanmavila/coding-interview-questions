def permute(string, frm=0):
	"""Return a list of all permutations of 'string'."""
	n = len(string)
	# Either the input string is empty, or we have
	# permuted every character except the last and
	# should stop.
	if frm >= n-1:
		return ["".join(string)]

	def swap(i, j):
		string[i], string[j] = \
			string[j], string[i]

	results = []
	# Swap every character in the range [from..end]
	# with the character at 'from', and permute the
	# range [from+1..end]
	for i in xrange(frm, n):
		# Handle duplicate entries
		if i != frm and string[i] == string[frm]:
			continue
		swap(i, frm)
		# It's important to create a new copy of 'string'
		# so that references from recursions do not
		# affect the local copy.
		results.extend(permute(list(string), frm+1))

	return results

if __name__ == "__main__":
	string = "abc" # 6 results
	string = "" # 1 result
	string = "a" # 1 result
	string = "aab" # 3 results
	string = "aabb" # 6 results
	for r in permute(list(string)):
		print r
