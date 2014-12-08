#Q3: Largest prime factor
import math, types

def primes_sieve(num):
	temp_primes = []
	remove = []
	upper_limit = int(math.ceil(num**.5))

	if num < 2:
		return 'no prime numbers found'
	else:
		#find all divisors
		for i in range(2, upper_limit):

			#check for divsors
			if num % i == 0:
				temp_primes.append(i)

		#check for more divisors	
		for n in temp_primes:
			divisor = num/n
			if divisor not in temp_primes:
				temp_primes.append(divisor)
			
		for n in temp_primes:
			for i in temp_primes:
				if n % i == 0 and n != i:
					if n not in remove:
						remove.append(n)

		for n in remove:
			if n in temp_primes:
				temp_primes.remove(n)


		if len(temp_primes) == 0:
			return num, 'is potentially a prime number'

		else:
			return 'all the prime divisors of ', num, ' are ', temp_primes

print primes_sieve(14)