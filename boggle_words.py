def make_words(boggle, dictionary):
	m = len(boggle)
	if m == 0: # Empty boggle
		return
	n = len(boggle[0])

	visited = [[False] * n for i in xrange(m)]

	# Recursive utility method for finding words (DFS)
	def _make_word(string, i, j):
		# Out of bounds
		if i < 0 or j < 0 or i == m or j == n:
			return

		# Already visited this cell
		if visited[i][j]:
			return

		# Check the newly formed word
		new_string = string + boggle[i][j]
		if new_string in dictionary:
			print new_string

		# Move to neighboring cells.
		# No need to check if visited
		visited[i][j] = True
		for k in [-1, 0, 1]:
			for l in [-1, 0, 1]:
				_make_word(new_string, i+k, j+l)
		visited[i][j] = False

	for i in xrange(m):
		for j in xrange(n):
			_make_word("", i, j)

if __name__ == "__main__":
	boggle = [
		['G','I','Z'],
		['U','E','K'],
		['Q','S','E']] # "GEEKS", "QUIZ"
	boggle = [
		['F'],
		['O'],
		['R']] # "FOR"
	boggle = [] # Nothing
	boggle = [[]] # Nothing
	boggle = ['A'] # "A"
	dictionary = ['A', 'GEEKS', 'FOR', 'QUIZ', 'GO']
	make_words(boggle, dictionary)
