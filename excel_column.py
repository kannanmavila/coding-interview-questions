def excel_column(n):
	column = ""
	while n > 0:
		n -= 1
		column += chr(ord('A') + (n % 26))
		n /= 26
	return column[::-1]

if __name__ == "__main__":
	columns = [26, 51, 52, 80, 676, 702, 705]
	for c in columns:
		print excel_column(c)
