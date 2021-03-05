def parse_ranges(ranges_string):
	ranges = (tuple(map(int, rng.split('-'))) for rng in ranges_string.split(','))
	return (num for start, stop in ranges for num in range(start, stop + 1))
