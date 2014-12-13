def spiral(n):

	output = []
	start = 0
	end = n/2

	for i in range(n*n):
		if i == 0:
			output.append((start, start))

		if i == (n-1):
			output.append((end, end))

		else:
			if i <= n*n/2:
				output.append()

	
	for o in output:
		print o

	return ''


print spiral(3)
