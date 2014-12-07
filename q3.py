#Q3: Largest prime factor
import math

def primes_sieve(num):
	prime_divisors = []

	if num < 2:
		return 'no prime numbers found'
	elif num == 2:
		return num,' is prime, with no other divisors'
	elif num == 3:
		return num,' is prime, with no other divisors'
	else:
		#find all divisors
		for i in range(2, int(math.ceil(num**.5))+2):
			#check for divsors
			if num % i == 0:
				print i, 'potential prime'
				#check for more primes
				if num/i
			#check which divisors are prime

		#return all prime divisors in an array

	return 'end of program'

print primes_sieve(14)