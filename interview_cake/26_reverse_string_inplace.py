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

if __name__ == "__main__":
	print reverse("abc")
	print reverse("abcd")
	print reverse("a")
	print reverse("")
