def reverse(string):
	string = list(string)
	length = len(string)
	for i in xrange((length - 1) / 2 + 1):
		string[i], string[length-i-1] = string[length-i-1],string[i]
	return "".join(string)

print reverse("Madam, I'm Adam")
