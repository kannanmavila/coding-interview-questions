class InvalidInput(Exception):
	pass


class TestFailure(Exception):
	pass


class ValueMismatch(TestFailure):
	pass


def fibonacci(n, recurse=True):
	if n < 0:
		raise InvalidInput("n cannot be negative")
	if n == 0:
		return 0
	if n == 1:
		return 1
	if recurse:
		return fibonacci(n-1) + fibonacci(n-2)
	return fibonacci_iterative(n)

def fibonacci_iterative(n):
	f_minus_2 = 0
	f_minus_1 = 1
	for i in range(2, n+1):
		f = f_minus_1 + f_minus_2
		f_minus_2 = f_minus_1
		f_minus_1 = f
	return f

if __name__ == "__main__":
	# Test recursive and iterative fibonacci methods
	for i in range(0, 30):
		recursive = fibonacci(i)
		iterative = fibonacci(i, recurse=False)
		if recursive != iterative:
			raise ValueMismatch(recursive, iterative)
			break
