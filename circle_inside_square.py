def draw_circle(r):
	for i in xrange(0, 2*r+2):
		line =["X" if (i-r) ** 2 + (j-r) ** 2 <= r ** 2 else " "						for j in xrange(0, 2*r+2)]
		print " ".join(line)

if __name__ == "__main__":
	draw_circle(20)
