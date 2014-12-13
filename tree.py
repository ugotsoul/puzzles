def christmas(n):

	space = ' '

	for i in range(n):

		if i == 0:
			print space*(n-1)+'$$'
		elif i < (n-1):
			print space*(n-i)+('/'+'\\')*i
			print space*(n-i)+('* ')*(i+1)
		else:
			print space*(n-1)+'||'
	return "Merry Christmas, ya jerk!"

print christmas(5)   