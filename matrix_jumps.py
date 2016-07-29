def jumps(m, n):
	if m < 1 or n < 1:
		return None
	count = 0
	while True:
		m, n = max(m, n), min(m, n) # Order doesn't matter
		if n == 0:
			return None
		if n == 1:
			return count + m - 1
		count += m / n
		m %= n

if __name__ == "__main__":
	inputs = [(7, 5), # 3
		(3, 10),  # 5
		(1, 2),   # 1
		(1, 1)]   # 0
	for i in inputs:
		print jumps(*i)
