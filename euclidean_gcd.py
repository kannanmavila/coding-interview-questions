def euclidean_gcd(m, n, *values):
	if values:
		n = euclidean_gcd(n, *values)
	while True:
		if 0 in (m, n):
			return max(m, n)
		m, n = max(m, n) % min(m, n), min(m, n)

if __name__ == "__main__":
	print euclidean_gcd(105, 252, 210)
