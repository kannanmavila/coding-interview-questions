class LengthMismatch(Exception):
	pass


class Non32Representation(Exception):
	pass


def ones(n):
	count = 0
	while n > 0:
		if n & 1: count += 1
		n >>= 1
	return count

def ones_optimized(n):
	count = 0
	while n > 0:
		n &= n-1
		count += 1
	return count

def binary(n):
	return bin(n)[2:]

def mask(n, m, i, j):
	if None in (m, n, i, j):
		return None
	nb, mb = binary(n), binary(m)
	if len(mb) != j-i+1:
		raise LengthMismatch(mb)
	mask = (2 ** (j - i + 1) - 1) * 2 ** i
	substr = m * 2 ** i + 2 ** (i - 1)
	return n | mask & substr

def float_binary(float):
	repr = []
	# Decimal part
	f = float % 1
	while f > 0:
		f *= 2
		repr.append(1 if f >= 1 else 0)
		f %= 1
	repr = repr[::-1]
	repr.append('.')
	i = int(float)
	# Whole part
	while i > 0:
		repr.append(1 if i & 1 else 0)
		i /= 2
	# Join, reverse(!), return
	repr = "".join(map(str, repr[::-1]))
	if len(repr) > 32:
		raise Non32Representation
	return repr

if __name__ == "__main__":
	for i in xrange(1000):
		if bin(i)[2:].count('1') != ones(i):
			print i

	#print binary(mask(1024, 21, 2, 6))
	print float_binary(11.25)
