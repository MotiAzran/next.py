def is_prime(number):
	# return all([number % x != 0 for x in range(2, number)])
	return len(range(2, number)) == len([x for x in range(2, number) if number % x != 0])
