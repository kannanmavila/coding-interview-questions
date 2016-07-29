def print_paths(grid):
	_print_paths(grid, 0, 0)

def _print_paths(grid, m, n, path=[]):
	try:
		if m == len(grid) - 1 and n == len(grid[m]) - 1:
			print "".join(path)
			return
		if grid[m][n] == 1:
			return
	except IndexError:
		return
	path.append("R")
	_print_paths(grid, m, n+1, path)
	path.pop()
	path.append("D")
	_print_paths(grid, m+1, n, path)
	path.pop()

if __name__ == "__main__":
	X = 1
	grid = [[0, 0, 0],
		[0, 0, X],
		[0, 0, 0]]
	print_paths(grid)
