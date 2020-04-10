import math


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

	@staticmethod
	def number_of_divisors(n):
		"""
		find the number of divisors for supplied n

		:param n: int
		:return: int
		"""
		result = 0
		sqrt = int(math.sqrt(n))
		for i in range(1, sqrt + 1):
			if n % i == 0:
				result += 2
		# if perfect square root, don't count twice
		if n == sqrt * sqrt:
			result -= 1
		return result
