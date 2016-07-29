def char_index(c, base='a'):
	return ord(c)-ord(base)

def first_unique_char(word):
	ht = [0]*26
	for i in word:
		ht[char_index(i)] += 1
	return next((i for i in word
			 if ht[char_index(i)] == 1), None)

if __name__ == "__main__":
	print first_unique_char("teeter")
