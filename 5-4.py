import functools


def str_int_sum(a, b):
	return int(a) + int(b)


def sum_of_digits(number):
	return int(functools.reduce(str_int_sum, str(number)))


def check_id_valid(id_number):
	res = []
	for i, digit in enumerate(map(int, str(id_number))):
		if i % 2 != 0:
			res.append(sum_of_digits(digit * 2))
		else:
			res.append(sum_of_digits(digit))

	return sum(res) % 10 == 0


def check_id_valid_with_generator(id_number):
	digits = (int(digit) for digit in str(id_number))
	mul_digits = (digit if i % 2 == 0 else digit * 2 for i, digit in enumerate(digits))
	sum_digits = (sum_of_digits(num) for num in mul_digits)

	return sum(sum_digits) % 10 == 0


class IDIterator(object):
	def __init__(self, id=100000000):
		self._id = id

	def __iter__(self):
		return self

	def __next__(self):
		self._id += 1
		while not check_id_valid(self._id) and self._id <= 999999999:
			self._id += 1

		if self._id > 999999999:
			raise StopIteration()

		return self._id


def id_generator(start_id):
	cur_id = start_id + 1
	while cur_id <= 999999999:
		if check_id_valid(cur_id):
			yield cur_id

		cur_id += 1


def check_user_input(user_input):
	if len(user_input) != 9:
		print("ID length should be 9")
		return False
	elif not user_input.isdigit():
		print("ID should contain only digits")
		return False
	elif int(user_input) < 100000000:
		print("ID should start with 1")
		return False

	return True


def main():
	user_input = input("Enter ID: ")
	if not check_user_input(user_input):
		return 1

	is_gen = input("Generator or Iterator? (gen/it)? ").lower() == "gen"

	if is_gen:
		id_gen = id_generator(int(user_input))
		for _ in range(10):
			print(next(id_gen))
	else:
		id_iter = IDIterator(int(user_input))
		for _ in range(10):
			print(next(id_iter))


if __name__ == '__main__':
	main()