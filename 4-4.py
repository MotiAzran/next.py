import calendar


def gen_secs():
	for sec in range(0, 60):
		yield sec


def gen_minutes():
	for minute in range(0, 60):
		yield minute


def gen_hours():
	for hour in range(0, 24):
		yield hour


def gen_time():
	for hour in gen_hours():
		for minute in gen_minutes():
			for sec in gen_secs():
				yield "{:02d}:{:02d}:{:02d}".format(hour, minute, sec)


def gen_years(start=2019):
	while True:
		yield start
		start += 1


def gen_months():
	for month in range(1, 13):
		yield month


def gen_days(month, leap_year=True):
	long_months = (1, 3, 5, 7, 8, 10, 12)
	short_months = (4, 6, 9, 11)

	if month == 2:
		stop = 29 if leap_year else 28
	elif month in long_months:
		stop = 31
	elif month in short_months:
		stop = 30
	else:
		raise ValueError("Month should be between 1 to 12")
	
	for day in range(1, stop + 1):
		yield day


def gen_date():
	for year in gen_years():
		for month in gen_months():
			for day in gen_days(month, leap_year=calendar.isleap(year)):
				for time in gen_time():
					yield "{:02d}/{:02d}/{:02d} {}".format(day, month, year, time)


def main():
	gd = gen_date()
	while True:
		for _ in range(1000000):
			next(gd)

		print(next(gd))


if __name__ == '__main__':
	main()
