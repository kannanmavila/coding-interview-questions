def fact(n):
	factors = []
	for i in xrange(2, n/2+1):
		if n % i == 0:
			factors.append(i)
	return factors

def calc_sequence(n, working):
	working = map(str, working)
	if set(list(str(n))) <= set(working):
		return len(str(n)), str(n)

	choice = None
	for p in fact(n):
		try:
			calc_p, seq_p = calc_sequence(p, working)
			calc_rest, seq_rest = calc_sequence(n/p, working)
			new_choice = calc_p + calc_rest + 1
			if choice is None or new_choice < choice:
				choice = new_choice
				seq = seq_p + " * " + seq_rest
		except TypeError:
			pass
	if choice is None:
		return None, None
	return choice, seq

if __name__ == "__main__":
	print calc_sequence(195, [1, 2, 3, 5, 7])[1]
	print calc_sequence(36, [1, 6])[1]
	print calc_sequence(400, [2, 0])[1]
	print calc_sequence(1111*1111, [1, 2])[1]
