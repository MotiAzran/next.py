def is_four_divider(num):
	return num % 4 == 0


def four_dividers(number):
	return list(filter(is_four_divider, range(1, number)))
