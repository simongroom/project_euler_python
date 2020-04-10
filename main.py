# coding=utf-8
import math

from helpers import Helpers


def even_fib_numbers():
	ef1 = 0
	ef2 = 2
	result = ef1 + ef2
	r = 4000000
	while ef2 <= r:
		ef3 = 4 * ef2 + ef1
		if ef3 > r:
			break
		result += ef3
		ef1 = ef2
		ef2 = ef3
	print(str(result))


def largest_prime_factor():
	n = 600851475143
	# n = 6
	result = -1
	while n % 2 == 0:
		result = 2
		n /= 2
		print("result is: " + str(result))
		print("n is: " + str(n))

	for i in range(3, int(math.sqrt(n)), 2):
		while n % i == 0:
			result = i
			n = n / i
			print("result is: " + str(result))
			print("n is: " + str(n))
	if n > 2:
		result = n
	print("result is: " + str(result))


def largest_palindrome_product():
	start = 100
	end = 999
	result = 0
	for x in range(end, start, -1):
		for y in range(end, start, -1):
			prod = x * y
			if str(prod) == str(prod)[::-1]:
				if prod > result:
					result = prod
	print("result: " + str(result))


def smallest_multiple():
	n = 20
	result = 1
	for x in range(1, n, 1):
		previous = result
		while result % x != 0:
			result = result + previous
	print("result: " + str(result))


def sum_square_difference():
	n = 100
	sum_squares = 0
	square_sums = 0
	for i in range(n + 1):
		sum_squares = sum_squares + (i * i)
	for i in range(n + 1):
		square_sums += i
	square_sums = square_sums * square_sums
	result = square_sums - sum_squares
	print(str(result))


def ten_thousand_first_prime():
	num_primes = 1
	counter = 2
	while num_primes < 10001:
		counter += 1
		if Helpers.is_prime(counter):
			num_primes += 1
	print(str(counter))


def largest_product_in_series():
	num = 7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450
	greatest_product = 0
	num_string = str(num)
	n_len = len(num_string)
	split_num = 13
	# split_num = 4
	for i in range(n_len - split_num + 1):
		portion = num_string[i:split_num + i]
		portion_list = [int(s) for s in portion]
		prod = 1
		for p in portion_list:
			prod = prod * p
		if prod > greatest_product:
			greatest_product = prod
	print(str(greatest_product))


def special_pythagorean_triplet():
	result = 0
	target = 1000
	for counter in range(1, target):
		if result != 0:
			break
		for counter_1 in range(counter + 1, target - 1):
			counter_2 = ((counter ** 2) + (counter_1 ** 2)) ** 0.5
			if counter + counter_1 + counter_2 == target:
				print("counter value is: " + str(counter))
				print("counter_1 value is: " + str(counter_1))
				print("counter_2 value is: " + str(counter_2))
				print("************HIT**************")
				result = counter * counter_1 * counter_2
				break
	Helpers.pr(int(result))


def summation_of_primes():
	"""
	The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

	Find the sum of all the primes below two million.
	:return:
	"""
	result = 0
	n = 2000000
	# n = 10
	for i in range(n):
		if Helpers.is_prime(i):
			result += i
	Helpers.pr(result)


def largest_product_in_a_grid():
	"""
	In the 20×20 grid below, four numbers along a diagonal line have been
	marked in red.

	08 02 22 97 38 15 00 40 00 75 04 05 07 78 52 12 50 77 91 08
	49 49 99 40 17 81 18 57 60 87 17 40 98 43 69 48 04 56 62 00
	81 49 31 73 55 79 14 29 93 71 40 67 53 88 30 03 49 13 36 65
	52 70 95 23 04 60 11 42 69 24 68 56 01 32 56 71 37 02 36 91
	22 31 16 71 51 67 63 89 41 92 36 54 22 40 40 28 66 33 13 80
	24 47 32 60 99 03 45 02 44 75 33 53 78 36 84 20 35 17 12 50
	32 98 81 28 64 23 67 10 26 38 40 67 59 54 70 66 18 38 64 70
	67 26 20 68 02 62 12 20 95 63 94 39 63 08 40 91 66 49 94 21
	24 55 58 05 66 73 99 26 97 17 78 78 96 83 14 88 34 89 63 72
	21 36 23 09 75 00 76 44 20 45 35 14 00 61 33 97 34 31 33 95
	78 17 53 28 22 75 31 67 15 94 03 80 04 62 16 14 09 53 56 92
	16 39 05 42 96 35 31 47 55 58 88 24 00 17 54 24 36 29 85 57
	86 56 00 48 35 71 89 07 05 44 44 37 44 60 21 58 51 54 17 58
	19 80 81 68 05 94 47 69 28 73 92 13 86 52 17 77 04 89 55 40
	04 52 08 83 97 35 99 16 07 97 57 32 16 26 26 79 33 27 98 66
	88 36 68 87 57 62 20 72 03 46 33 67 46 55 12 32 63 93 53 69
	04 42 16 73 38 25 39 11 24 94 72 18 08 46 29 32 40 62 76 36
	20 69 36 41 72 30 23 88 34 62 99 69 82 67 59 85 74 04 36 16
	20 73 35 29 78 31 90 01 74 31 49 71 48 86 81 16 23 57 05 54
	01 70 54 71 83 51 54 69 16 92 33 48 61 43 52 01 89 19 67 48

	The product of these numbers is 26 * 63 * 78 * 14 = 1788696.

	What is the greatest product of four adjacent numbers in the same
	direction (up, down, left, right, or diagonally) in the 20×20 grid?
	:return:
	"""
	def get_point_value(multi_dim_arr, y_el, x_el):
		if 0 <= y_el < len(multi_dim_arr) and 0 <= x_el < len(multi_dim_arr[y_el]):
			return multi_dim_arr[y_el][x_el]
		return 0

	result = 0
	arr = [
		[8, 02, 22, 97, 38, 15, 00, 40, 00, 75, 04, 05, 07, 78, 52, 12, 50, 77,
			91, 8],
		[49, 49, 99, 40, 17, 81, 18, 57, 60, 87, 17, 40, 98, 43, 69, 48, 04, 56,
			62, 00],
		[81, 49, 31, 73, 55, 79, 14, 29, 93, 71, 40, 67, 53, 88, 30, 03, 49, 13,
			36, 65],
		[52, 70, 95, 23, 04, 60, 11, 42, 69, 24, 68, 56, 01, 32, 56, 71, 37, 02,
			36, 91],
		[22, 31, 16, 71, 51, 67, 63, 89, 41, 92, 36, 54, 22, 40, 40, 28, 66, 33,
			13, 80],
		[24, 47, 32, 60, 99, 03, 45, 02, 44, 75, 33, 53, 78, 36, 84, 20, 35, 17,
			12, 50],
		[32, 98, 81, 28, 64, 23, 67, 10, 26, 38, 40, 67, 59, 54, 70, 66, 18, 38,
			64, 70],
		[67, 26, 20, 68, 02, 62, 12, 20, 95, 63, 94, 39, 63, 8, 40, 91, 66, 49,
			94, 21],
		[24, 55, 58, 05, 66, 73, 99, 26, 97, 17, 78, 78, 96, 83, 14, 88, 34, 89,
			63, 72],
		[21, 36, 23, 9, 75, 00, 76, 44, 20, 45, 35, 14, 00, 61, 33, 97, 34, 31,
			33, 95],
		[78, 17, 53, 28, 22, 75, 31, 67, 15, 94, 03, 80, 04, 62, 16, 14, 9, 53,
			56, 92],
		[16, 39, 05, 42, 96, 35, 31, 47, 55, 58, 88, 24, 00, 17, 54, 24, 36, 29,
			85, 57],
		[86, 56, 00, 48, 35, 71, 89, 07, 05, 44, 44, 37, 44, 60, 21, 58, 51, 54,
			17, 58],
		[19, 80, 81, 68, 05, 94, 47, 69, 28, 73, 92, 13, 86, 52, 17, 77, 04, 89,
			55, 40],
		[04, 52, 8, 83, 97, 35, 99, 16, 07, 97, 57, 32, 16, 26, 26, 79, 33, 27,
			98, 66],
		[88, 36, 68, 87, 57, 62, 20, 72, 03, 46, 33, 67, 46, 55, 12, 32, 63, 93,
			53, 69],
		[04, 42, 16, 73, 38, 25, 39, 11, 24, 94, 72, 18, 8, 46, 29, 32, 40, 62,
			76, 36],
		[20, 69, 36, 41, 72, 30, 23, 88, 34, 62, 99, 69, 82, 67, 59, 85, 74, 04,
			36, 16],
		[20, 73, 35, 29, 78, 31, 90, 01, 74, 31, 49, 71, 48, 86, 81, 16, 23, 57,
			05, 54],
		[01, 70, 54, 71, 83, 51, 54, 69, 16, 92, 33, 48, 61, 43, 52, 01, 89, 19,
			67, 48]
	]
	d = 4
	for y in range(len(arr)):
		for x in range(len(arr)):
			point1, point2, point3, point4 = 1, 1, 1, 1
			for i in range(d):
				print("point1: " + str(point1))
				print("point2: " + str(point2))
				print("point3: " + str(point3))
				print("point4: " + str(point4))
				point1 *= get_point_value(arr, y, x + i)
				point2 *= get_point_value(arr, y + i, x)
				point3 *= get_point_value(arr, y + i, x + i)
				point4 *= get_point_value(arr, y + i, x - i)
				print("point1: " + str(point1))
				print("point2: " + str(point2))
				print("point3: " + str(point3))
				print("point4: " + str(point4))
				result = max(point1, point2, point3, point4, result)
				Helpers.pr(result)

	Helpers.pr(result)


def highest_divisible_triangular_number():
	"""
	The sequence of triangle numbers is generated by adding the natural numbers.
	So the 7th triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28.

	The first ten terms would be:

	1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

	Let us list the factors of the first seven triangle numbers:

	1: 1
	3: 1,3
	6: 1,2,3,6
	10: 1,2,5,10
	15: 1,3,5,15
	21: 1,3,7,21
	28: 1,2,4,7,14,28
	We can see that 28 is the first triangle number to have over five divisors.

	What is the value of the first triangle number to have over five
	hundred divisors?

	:return:
	"""
	target = 500
	result = 0
	n = 1
	while Helpers.number_of_divisors(result) < target:
		result += n
		n += 1
	Helpers.pr(result)


if __name__ == '__main__':
	# even_fib_numbers()
	# largest_prime_factor()
	# largest_palindrome_product()
	# smallest_multiple()
	# sum_square_difference()
	# ten_thousand_first_prime()
	# largest_product_in_series()
	# special_pythagorean_triplet()
	# summation_of_primes()
	# largest_product_in_a_grid()
	highest_divisible_triangular_number()
