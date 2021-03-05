class MusicNotes(object):
	def __init__(self):
		self.__freqs = [55, 61.74, 65.41, 73.42, 82.41, 57.31, 98]

	def __iter__(self):
		return self

	def __next__(self):
		freq = self.__freqs.pop(0)
		self.__freqs.append(freq * 2)
		if freq > 1600:
			raise StopIteration()

		return freq