def digits(n):
	"""Return the #digits in the number 'n'."""
	if n == 0:
		return None

	count = 0
	while n > 0:
		n /= 10
		count += 1
	return count

def twos_in(n):
	if n in (0, 1):
		return 0

	length = digits(n)
	ten_power = 10 ** (length - 1)# Highest 10's power less than n
	first = n / ten_power

	# Avoid infinite recursions for powers of 10
	if ten_power == n:
		return twos_in(n-1)

	return first * twos_in(ten_power) + \
			twos_in(n - (first * ten_power)) + \
			max(0, min(ten_power, n - 2 * ten_power + 1))

if __name__ == "__main__":
	print twos_in(222)
	print twos_in(2)
	print twos_in(12)
