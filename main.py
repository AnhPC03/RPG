import os
import gmpy2
import timeit
from time import time
from gmpy2 import xmpz, mpz


# 400 first prime numbers
prime_arr = [
2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71,
73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173,
179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281,
283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409,
419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 199, 503, 509, 521, 523, 541,
547, 557, 563, 569, 571, 577, 587, 593, 599, 601, 607, 613, 617, 619, 631, 641, 643, 647, 653, 659,
661, 673, 677, 683, 691, 701, 709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787, 797, 809,
811, 821, 823, 827, 829, 839, 853, 857, 859, 863, 877, 881, 883, 887, 907, 911, 919, 929, 937, 941,
947, 953, 967, 971, 977, 983, 991, 997, 1009, 1013, 1019, 1021, 1031, 1033, 1039, 1049, 1051, 1061, 1063, 1069,
1087, 1091, 1093, 1097, 1103, 1109, 1117, 1123, 1129, 1151, 1153, 1163, 1171, 1181, 1187, 1193, 1201, 1213, 1217, 1223,
1229, 1231, 1237, 1249, 1259, 1277, 1279, 1283, 1289, 1291, 1297, 1301, 1303, 1307, 1319, 1321, 1327, 1361, 1367, 1373,
1381, 1399, 1409, 1423, 1427, 1429, 1433, 1439, 1447, 1451, 1453, 1459, 1471, 1481, 1483, 1487, 1489, 1493, 1499, 1511,
1523, 1531, 1543, 1549, 1553, 1559, 1567, 1571, 1579, 1583, 1597, 1601, 1607, 1609, 1613, 1619, 1621, 1627, 1637, 1657,
1663, 1667, 1669, 1693, 1697, 1699, 1709, 1721, 1723, 1733, 1741, 1747, 1753, 1759, 1777, 1783, 1787, 1789, 1801, 1811,
1823, 1831, 1847, 1861, 1867, 1871, 1873, 1877, 1879, 1889, 1901, 1907, 1913, 1931, 1933, 1949, 1951, 1973, 1979, 1987,
1993, 1997, 1999, 2003, 2011, 2017, 2027, 2029, 2039, 2053, 2063, 2069, 2081, 2083, 2087, 2089, 2099, 2111, 2113, 2129,
2131, 2137, 2141, 2143, 2153, 2161, 2179, 2203, 2207, 2213, 2221, 2237, 2239, 2243, 2251, 2267, 2269, 2273, 2281, 2287,
2293, 2297, 2309, 2311, 2333, 2339, 2341, 2347, 2351, 2357, 2371, 2377, 2381, 2383, 2389, 2393, 2399, 2411, 2417, 2423,
2437, 2441, 2447, 2459, 2467, 2473, 2477, 2503, 2521, 2531, 2539, 2543, 2549, 2551, 2557, 2579, 2591, 2593, 2609, 2617,
2621, 2633, 2647, 2657, 2659, 2663, 2671, 2677, 2683, 2687, 2689, 2693, 2699, 2707, 2711, 2713, 2719, 2729, 2731, 2741
]


def checkFermat(n):
	if gmpy2.powmod(2, n-1, n) != 1:
		return 1
	return 0

def algorithmWitness(a, n):
	t = 0
	u = n-1
	while gmpy2.f_mod(n, 2) == 0:
		u = u >> 1
		t += 1
	x_0 = gmpy2.powmod(a, u, n)
	for i in range(1, t+1):
		x_1 = gmpy2.powmod(x_0, 2, n)
		if x_1 == 1 and x_0 != 1 and x_0 != (n-1):
			return 1
		x_0 = x_1
	if x_0 != 1:
		return 1
	else:
		return 0

def algorithmRabin_Miller(n, s):
	random_state = gmpy2.random_state(int(round(time() * 1000)))
	for j in range (1, s+1):
		a = gmpy2.mpz_random(random_state, n)
		if algorithmWitness(a, n) == 1:
			return 1
	return 0

def advanceRabin_Miller(n):
	for prime_number in prime_arr:
		if gmpy2.f_mod(n, prime_number) == 0:
			return 1
	if checkFermat(n) == 1:
		return 1
	if algorithmRabin_Miller(n, 64) == 1:
		return 1
	return 0
# print(algorithmRabin_Miller(887, 10))

if __name__ == '__main__':
	count_numbers = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
	i = 0
	start = timeit.default_timer()
	start_total = start
	while True:
		if i == 100:
			break
		randbytes = os.urandom(384)
		randnumber = int.from_bytes(randbytes, 'big')
		randnumber = xmpz(randnumber)
		randnumber[0] = 1
		randnumber[3071] = 1

		# print(randnumber)

		if advanceRabin_Miller(randnumber) == 0:
			i += 1
			stop = timeit.default_timer()
			took_time = stop - start
			start = timeit.default_timer()
			print(took_time)
			if 0 < took_time and took_time <= 1:
				count_numbers[0] += 1
			elif 1 < took_time and took_time <= 2:
				count_numbers[1] += 1
			elif 2 < took_time and took_time <= 3:
				count_numbers[2] += 1
			elif 3 < took_time and took_time <= 4:
				count_numbers[3] += 1
			elif 4 < took_time and took_time <= 5:
				count_numbers[4] += 1
			elif 5 < took_time and took_time <= 6:
				count_numbers[5] += 1
			elif 6 < took_time and took_time <= 7:
				count_numbers[6] += 1
			elif 7 < took_time and took_time <= 8:
				count_numbers[7] += 1
			elif 8 < took_time and took_time <= 9:
				count_numbers[8] += 1
			elif 9 < took_time and took_time <= 10:
				count_numbers[9] += 1
			# print(f'{i} - {len(str(bin(randnumber)[2:]))}')
			# print(randnumber)
			# print(gmpy2.is_prime(randnumber))
	
	stop_total = timeit.default_timer()
	for j in range(0, 10):
		print(f'number of numbers in {j} - {j+1} is: {count_numbers[j]} \n')

	print(f'The average time to generate each prime number of the 100 first prime numbers is: {(stop_total - start_total) / 100}\n')