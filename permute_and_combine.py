def swap(string, pos1, pos2):
	if pos1 == pos2:
		return string
	return string[0:pos1] + string[pos2] + string[pos1+1:pos2] + string[pos1] + string[pos2+1:]

def permute(string, pos=0):
	if pos == len(string)-1:
		print string
		return
	for i in xrange(len(string)-pos):
		permute(swap(string, pos, pos+i), pos+1)

def r_combine(string, pos, comb):
	if pos == len(string):
		print comb
		return
	r_combine(string, pos+1, comb+string[pos])
	r_combine(string, pos+1, comb)

def combine(string):
	r_combine(string, 0, "")

if __name__ == "__main__":
	permute("1234")
	#combine("1234")
