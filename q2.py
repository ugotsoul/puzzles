#makes a list of fibonacci numbers
def make_fibs(limit):
	fib_list = [1, 2]
	i = 1

	#case 1:
	if limit == 1:
		return fib_list[0]

	#case 2:
	if limit == 2:
		return fib_list

	#case 3: add sum of previous two items (from the end of the list) to the list
	else:
		while fib_list[-1] + fib_list[-2] < limit:
			fib_list.append(fib_list[-1] + fib_list[-2])
			i+=1	
		return fib_list

def get_even_fibs(fib_list):
	even_fib_list = []
	i = 0

	while i < len(fib_list):
		if fib_list[i] % 2 == 0:
			even_fib_list.append(fib_list[i])
			i+=1
		else:
			i+=1

	return even_fib_list


def sum_of_fibs(even_fib_list):
	accum = 0
	i = 0

	for i in range(len(even_fib_list)):
		accum += even_fib_list[i]
		i+=1
	
	return accum

def make_even_fib_sum(limit):
	list_fibs = make_fibs(limit)
	list_even_fibs = get_even_fibs(list_fibs)
	sum_even_fibs = sum_of_fibs(list_even_fibs)
	
	return sum_even_fibs

print make_even_fib_sum(4000000)