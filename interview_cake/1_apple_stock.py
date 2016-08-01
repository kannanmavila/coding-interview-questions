class InvalidPrices(ValueError):
    pass


def max_profit(prices):
    """Returns the maximum profit that can be made from yesterday’s stock."""
    if len(prices) < 2:
        raise InvalidPrices(prices)

    min_price = prices[0]
    max_profit = None
    for i in xrange(1, len(prices)):
        max_profit = max(max_profit, prices[i] - min_price)
        min_price = min(min_price, prices[i])
    return max_profit

print max_profit([10, 7, 5, 8, 11, 9])

