DECK_SIZE = 8

def is_single_riffle(deck, half1, half2):
	assert len(deck) == DECK_SIZE, \
			"Deck should contain %d cards." % DECK_SIZE
	assert len(half1) + len(half2) == DECK_SIZE, \
			"Halves should sum up to %d." % DECK_SIZE

	half1_pointer = half2_pointer = 0
	for i in xrange(DECK_SIZE):
		if half1_pointer < len(half1) and \
				deck[i] == half1[half1_pointer]:
			half1_pointer += 1
		elif half2_pointer < len(half2) and \
				deck[i] == half2[half2_pointer]:
			half2_pointer += 1
		else:
			return False
	return True

if __name__ == "__main__":
	deck = [1, 2, 3, 4, 5, 6, 7, 8]
	half1 = [1, 5, 6, 7, 8]
	half2 = [2, 3, 4]
	print is_single_riffle(deck, half1, half2) # False
