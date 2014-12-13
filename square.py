
def fibs(n):

	base = [1, 2]

	if n > 2:
		
		for i in range(n-2):
			base.append(base[-1]+base[-2])
			
		return base[-1]


def spiral(n):
	"""Returns a spiral drawn in the terminal, from left to right"""

	tail = ''
	middle = n - n/2 -1
	left = '<' + ' '
	right = '>' + ' '
	down = 'V' + ' '
	up = '^' + ' '
	empty = ' '


	if n:
		
		for i in range(n):

			if i == 0:
				#first line (n-1) left, (1) down
				tail += '\n'
				tail += right*(n-1) + down

			if i == middle:
				tail += '\n'
				
				if n > 3:
					tail += up+right*(middle)+empty*(middle)+down
				else:
					tail += up+right*(middle)+down

			elif i % 2 != 0:
				
				tail += '\n'

				if i - middle > 0:
					tail += up+empty*(n)+' '+down
				else:
					tail += empty*(n)+down


			if i == (n-1):				
				#last line
				tail += '\n' 
				tail += up + left*(n-1)

	#print first line, second line, third line (line range length is n+1)
	print tail

	return ''


print spiral(5)