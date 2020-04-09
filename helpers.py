
class Helpers:
	def __init__(self):
		pass

	@staticmethod
	def pr(r):
		print("result is: " + str(r))

	@staticmethod
	def is_prime(n):
		if n < 2:
			return False
		if n == 2 or n == 3:
			return True
		if n % 2 == 0:
			return False
		if n % 3 == 0:
			return False

		check = range(2, int(n ** .5) + 1)
		for i in check:
			if n % i == 0:
				return False
		return True
