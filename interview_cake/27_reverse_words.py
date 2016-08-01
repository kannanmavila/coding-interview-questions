class InvalidString(ValueError):
	pass


def reverse(string):
	if string is None:
		raise InvalidString(string)

	string = list(string)
	n = len(string)
	middle = n/2
	for i in xrange(middle):
		string[i], string[n-i-1] = \
			string[n-i-1], string[i]
	return "".join(string)

def reverse_words(string):
	string = list(string)
	start = end = 0
	n = len(string)
	while end < n:
		if string[end] == " ":
			string[start:end] = \
				reverse(string[start:end])
			start = end = end + 1
		end += 1
	# Last word
	string[start:end] = reverse(string[start:end])

	# Reverse entire string
	string = string[::-1]
	return "".join(string)

if __name__ == "__main__":
	string = "find you will pain only go you recordings security the into if"
	print reverse_words(string)
