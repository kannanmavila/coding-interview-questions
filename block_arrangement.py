class ArrangementDoesNotExist(ValueError):
	pass


class BlockSet(object):
	"""A set of blocks with heights from 1 .. N.

	Attributes:
		n: Number of blocks (aka height of the tallest block)

	"""
	def __init__(self, n):
		self.n = n

	def arrangements(self, left, right):
		"""Return the #arrangements with left and right visibility.

		Args:
			left: #blocks visible from left
			right: #blocks visible from right

		"""
		if (left + right) > (self.n + 1):
			raise ArrangementDoesNotExist(self.n, left, right)
		count = 0
		n = self.n
		for k in xrange(left-1, n-right+1):
			count += C(n-1, k) * \
					BlockSet._f(k, left-1) * \
					BlockSet._f(n-k-1, right-1)
		return count

	@staticmethod
	def _f(n, side):
		"""Return the #arrangements of n blocks with `side` visible
			from a side.

		Args:
			n: total #blocks
			side: #blocks visible from a side
		"""
		if n == 0: return 1
		if side == 0: return 0

		count = 0
		for k in xrange(side-1, n):
			count += C(n-1, k) * \
					BlockSet._f(k, side-1) * \
					fact(n-k-1)
		return count

def C(n, r):
	if n == 0: return 1
	return fact(n) / (fact(r) * fact(n-r))

def fact(n):
	if n == 0: return 1
	fact = 1
	for i in xrange(1, n+1):
		fact *= i
	return fact

if __name__ == "__main__":
	set = BlockSet(5)
	print set.arrangements(1, 4)
