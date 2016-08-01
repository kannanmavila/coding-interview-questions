class Meeting(object):
	"""A team-meeting.

	Attributes:
		start - start time of the meeting
		end - end time of the meeting

	"""
	def __init__(self, start, end):
		self.start = start
		self.end = end

	def __cmp__(self, other):
		return cmp(self.start, other.start)


class InvalidMeetings(ValueError):
	pass


def merged_meetings(meetings):
	"""Return a list of merged meetings, where each meeting
	is a possible combination of multiple meetings that collectively
	spanned	the same amount of time.

	"""
	if not meetings:
		raise InvalidMeetings()

	# Sort meetings by start times
	meetings = sorted([Meeting(s, e) for s, e in meetings])
	merged = []
	current = Meeting(meetings[0].start, meetings[0].end)

	# For every meeting, starting from the second
	for m in meetings[1:]:
		# Try and merge meetings
		if current.end >= m.start:
			current.end = max(current.end, m.end)
		# If distinct, add to the result
		else:
			merged.append(current)
			current = Meeting(m.start, m.end)
	# Last distinct meeting hasn't been added yet
	merged.append(current)
	return [(m.start, m.end) for m in merged]

print merged_meetings([(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)])
		# [(0, 1), (3, 8), (9, 12)]
print merged_meetings([(1, 2), (2, 3)]) # [(1, 3)]
print merged_meetings([(1, 5), (2, 3)]) # [(1, 5)]
print merged_meetings([(1, 10), (2, 6), (3, 5), (7, 9)])
		# [(1, 10)]
