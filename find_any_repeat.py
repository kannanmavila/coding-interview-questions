"""This can be achieved by negating the element at ith index for every
element i in the array, and then return an index if the element is
found to be negative."""

def find_repeat(the_list):
    floor = 1
    ceiling = len(the_list) - 1

    while floor < ceiling:

        # divide our range 1..n into an upper range and lower range
        # (such that they don't overlap)
        # lower range is floor..midpoint
        # upper range is midpoint+1..ceiling
        midpoint = floor + ((ceiling - floor) / 2)
        lower_range_floor, lower_range_ceiling = floor, midpoint
        upper_range_floor, upper_range_ceiling = midpoint+1, ceiling

        # count number of items in lower range
        items_in_lower_range = 0
        for item in the_list:
            # is it in the lower range?
            if item >= lower_range_floor and item <= lower_range_ceiling:
                items_in_lower_range += 1

        distinct_possible_integers_in_lower_range = \
            lower_range_ceiling - lower_range_floor + 1

        if items_in_lower_range > distinct_possible_integers_in_lower_range:
            # there must be a duplicate in the lower range
            # so use the same approach iteratively on that range
            floor, ceiling = lower_range_floor, lower_range_ceiling
        else:
            # there must be a duplicate in the upper range
            # so use the same approach iteratively on that range
            floor, ceiling = upper_range_floor, upper_range_ceiling


    # floor and ceiling have converged
    # we found a number that repeats!
    return floor

if __name__ == "__main__":
	print find_repeat([2, 2, 3])
