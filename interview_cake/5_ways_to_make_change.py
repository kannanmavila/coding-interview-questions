def ways_to_make_change_bottom_up(n, denominations):
	"""O(Nk) solution - uses the coins bottom-up.
	Start with a particular coin, update all amounts
	up till n, and never come back to that coin again.

	"""
	ways = [1] + [0] * n
	for coin in denominations:
		# For amounts higher than coin
		for amount in xrange(coin, n+1):
			# No. of ways you can make amount
			# using coins used so far, plus
			# new ways by using this'coin' and
			# making the remainder in its own ways
			ways[amount] += ways[amount-coin]
	return ways[n]

print ways_to_make_change_bottom_up(5, [1, 3, 5]) # 3
print ways_to_make_change_bottom_up(4, [1, 3, 5]) # 2
print ways_to_make_change_bottom_up(4, [1, 3, 2]) # 4
