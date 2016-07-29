def print_bracket_pairs(n, lefts=0, expression=""):
	if len(expression) == 2*n:
		print expression
		return
	if lefts < n:
		print_bracket_pairs(n, lefts+1, expression+"(")
	if lefts > len(expression)/2:
		print_bracket_pairs(n, lefts, expression+")")

if __name__ == "__main__":
	print_bracket_pairs(3)
