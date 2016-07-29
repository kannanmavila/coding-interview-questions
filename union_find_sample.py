class CycleFound(ValueError):
	pass


def has_cycle(edges):
	groups = {}
	for i, j in edges:
		# Connecting two points in the same set
		# creates a cycle.
		if i in groups.setdefault(j, [j]) \
				or j in groups.setdefault(i, [i]):
			return True

		# Union the subsets
		groups[i].extend(groups[j])
		groups[j] = groups[i]
	return False

if __name__ == "__main__":
	edges = [
		[0, 1],
		[2, 0],
		[0, 3],
		[2, 3]]
	edges = [
		[0, 1],
		[2, 0],
		[2, 1]]
	print "Graph", ("has a" if has_cycle(edges) \
			else "hasn't any"), "cycle"
