def find_largest_palindrome_product(digits):

	#largest palindromes:
	#Note: num of digits * 2 = largest palindrome made if num of digits > 1.
	#4 Digit: 91*99 = 9009 largest
	#6 Digit: what is the largest? brute force: start with 999,999

	min_palindrome = 100
	max_palindrome = 999
	num1 = 99
	num2 = 99
	product = num1*num2;
	list_product = [x for x in str(product)]

	print list_product

	#check first two of list
	first_half = list_product[:digits/2]
	print 'first half is: ', first_half

	#check last two of list
	second_half = list_product[(digits/2+1):(digits/2-1):-1]
	print 'second half is: ', second_half


	if first_half == second_half and list_product < digits:
		return 'yay,this is a palindrome!'

	else:
		return 'Not a palindrome'


	
print find_largest_palindrome_product()