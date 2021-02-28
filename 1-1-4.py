import functools


def str_int_sum(a, b):
	return int(a) + int(b)


def sum_of_digits(number):
	return functools.reduce(str_int_sum, str(number))
