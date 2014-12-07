#multiples of 3 and 5

def three_and_five_multiples(num): 
	
	i = 0
	accum = 0
	
	while i < num:

		if i % 3 == 0 or i % 5 == 0:	
			accum += i
			i+=1

		else:
			i+=1

	return accum

print three_and_five_multiples(1000)
