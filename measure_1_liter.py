class Vessel(object):
	def __init__(self, capacity, quantity=0):
		self.capacity = capacity
		self.quantity = quantity

	def fill(self):
		self.quantity = self.capacity

	def empty(self):
		self.quantity = 0

	@property
	def is_empty(self):
		return self.quantity == 0

	@property
	def is_full(self):
		return self.quantity == self.capacity

	def transfer_to(self, vessel):
		amount = min(self.quantity, vessel.capacity - vessel.quantity)
		self.quantity -= amount
		vessel.quantity += amount


def measure_one(m, n):
	m, n = Vessel(min(m, n)), Vessel(max(m, n))
	while m.quantity != 1:
		if m.is_empty: m.fill()
		if n.is_full: n.empty()
		m.transfer_to(n)
		print m.quantity, n.quantity

if __name__ == "__main__":
	measure_one(7, 3)
