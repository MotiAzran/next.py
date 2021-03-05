def get_fibo():
	x, y = 0, 1

	yield x
	yield y

	while True:
		yield x + y
		x, y = y, x + y
