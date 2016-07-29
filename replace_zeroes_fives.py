def replace_zeros(n, r):
	"""Replace zeroes in `n` with digit `r`."""
	if n == 0:
		return r

	value = 0
	pos = 0
	while n > 0:
		digit = n%10
		if digit == 0:
			digit = r
		value += digit * (10 ** pos)
		n /= 10
		pos += 1
	return value

if __name__ == "__main__":
	print replace_zeros(505, 5)
