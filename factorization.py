def fact(n):
	factors = []
	for i in xrange(2, n/2+1):
		if n % i == 0:
			factors.append(i)
	return [1] + factors + ([n] if n > 1 else [])

def prime_fact(n):
	factors = []

	for i in xrange(2, int(n ** .5)+1):
		while n % i == 0:
			factors.append(i)
			n /= i

	# n is a prime
	if n > 1:
		return [n]
	return factors

if __name__ == "__main__":
	print fact(1024)
	print prime_fact(1024)
