"""DOES NOT WORK! You need to maintain heaps for min and max balances
and keep inserting people back after each settlement. This is because after a settlent, the highest_creditor and lowest_debiter may have balance left,
but they may not hold the highest/lowest position anymore."""

class Person(object):
	def __init__(self, name, balance):
		self.name = name
		self.balance = balance

	def __cmp__(self, other):
		return cmp(self.balance, other.balance)


def settlements(debts):
	"""Print a set of settlements optimized for number thereof.

	Logic: Sort by net balance and keep settling the highest creditor
	from lowest debiter.

	"""
	n = len(debts) # No. of people

	# Find net balances of people
	# Store indices so that people
	# can be recognized after sorting
	net_balance = [None] * n
	for i in xrange(n):
		net_balance[i] = Person(i, sum([debts[j][i] - debts[i][j]
				for j in xrange(n)]))
	net_balance.sort()

	# Greedy settlement
	lowest_debiter = 0
	highest_creditor = n-1
	while True:
		debiter = net_balance[lowest_debiter]
		creditor = net_balance[highest_creditor]
		settlement = min(-debiter.balance, creditor.balance)

		# If noone owes, no one gets paid, and we're done
		if debiter.balance == 0 or creditor.balance == 0:
			return

		# Settle
		debiter.balance += settlement
		creditor.balance -= settlement
		print "%s pays %s: %s" % (debiter.name,
				creditor.name, settlement)

		# Relieve people with no balance
		if debiter.balance == 0:
			lowest_debiter += 1
		if creditor.balance == 0:
			highest_creditor -= 1

if __name__ == "__main__":
	debts = [
		[0, 1, 2],
		[0, 0, 5],
		[0, 0, 0]]
	debts = [
		[0]]
	debts = [
		[0, 1, 0],
		[0, 0, 1],
		[2, 0, 0]]
	debts = [
		[0, 1],
		[2, 0]]
	settlements(debts)
