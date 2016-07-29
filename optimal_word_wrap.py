def line_break_cost(string, m):
	"""Return the minimal cost of word wrapping, such that
	no line exceeds 'm' in length.

	"""
	# Mark the spaces
	n = len(string)
	length = [-1] + \
			[i for i in xrange(n) if string[i] == " "] + \
			[n] # Do not forget the last line

	# Iteratively assess costs
	spaces = len(length)
	cost = [(0, -1)] * spaces
	for i in xrange(1, spaces): # For every space
		choices = []
		for j in xrange(i-1, -1, -1): # For every previous space
			# Go back no more than m characters
			if length[j] < length[i] - m - 1:
				break
			wrap_cost = cost[j][0] + (m - length[i] + \
					length[j] + 1) ** 3
			choices.append((wrap_cost, j)) # (cost, choice)
		cost[i] = min(choices)

	# Print the solution
	wrapped = list(string)
	breaks = []
	position = spaces-1
	while cost[position][1] != 0:
		position = cost[position][1]
		wrapped[length[position]] = '\n'
	print "".join(wrapped)
	return cost[spaces-1][0]

if __name__ == "__main__":
	string = "aaa bb cc ddddd"
	print line_break_cost(string, 6) # 29
	string = "Geeks for Geeks presents word wrap problem"
	print line_break_cost(string, 15) # 13
	string = "Mel eu illum vivendum, in inani simul epicurei sea. Mea aperiam constituam ut, delenit delicata vix an. No causae epicurei duo, elit graeci similique cum te. Ad mea viris fastidii percipit. Omnesque complectitur mei ea, cum quas suscipit id. Nec cu semper saperet, legimus inciderint ei cum, sit ut tale mazim. Pri alienum gloriatur cu, no cetero ancillae quaerendum sed. Ex posse dignissim pri. Cu vel aperiri suscipit, novum dicit cetero ea pri. Populo albucius placerat ne eos, at dolor facete est."
	print line_break_cost(string, 60)
