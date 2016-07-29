def arrange_queens(n=8, board=None, column=0):
	def print_board():
		"""Pretty-prints a board."""
		for row in board:
			print " ".join(row)
		print

	def has_threat(board, row):
		"""Checks if a queen at (row, column) is under threat."""
		if 'Q' in board[row]:
			return True
		for i in range(len(board)):
			for j in range(len(board[i])):
				if j-column in (row-i, i-row) and \
						board[i][j] == 'Q':
					return True
		return False

	# Standard 8x8 board
	if board is None:
		board = [['-' for i in xrange(n)] for j in xrange(n)]

	# Done
	if n == 0:
		print_board()
		return 1

	# Arrange
	count = 0
	for i in range(len(board)):
		if not has_threat(board, i):
			board[i][column] = 'Q'
			count += arrange_queens(n-1, board, column+1)
			board[i][column] = '-'
	return count

if __name__ == "__main__":
	print arrange_queens(8)
