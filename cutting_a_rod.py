class InvalidLookup(ValueError):
	pass


class InvalidInput(ValueError):
	pass


class Rod(object):
	def __init__(self, length, price):
		self.length = length
		self.price = price

	@classmethod
	def from_prices(cls, prices):
		if not prices:
			raise InvalidInput(prices)
		return [cls(i+1, prices[i]) for i in xrange(len(prices))]


class PriceLookup(object):
	def __init__(self, rods):
		self.lookup = [None]*len(rods)
		self.lookup[0] = rods[0].price

	def get(self, i):
		if i == 0:
			return 0
		try:
			return self.lookup[i-1]
		except IndexError:
			raise InvalidLookup(i)

	def set(self, i, value):
		try:
			self.lookup[i-1] = value
		except IndexError:
			raise InvalidLookup(i)

	@property
	def result(self):
		return self.lookup[-1]

def max_cut_price(prices):
	# TODO Check for edge cases
	n = len(prices)
	rods = Rod.from_prices(prices)
	lookup = PriceLookup(rods)
	for i in xrange(1, n+1):
		choices = [lookup.get(j) + lookup.get(i-j)
					for j in xrange(1, i/2+1)]
		choices.append(lookup.get(0) + rods[i-1].price)
		lookup.set(i, max(choices))
	return lookup.result

if __name__ == "__main__":
	prices = [1, 5, 8, 9, 10, 17, 17, 20]
	print max_cut_price(prices)
