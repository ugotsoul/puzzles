def locker_business(num_of_lockers, num_of_people):

	#open locker == 0, closed == 1
	lockers = []
	people_counter = 0
	
	#make the lockers
	for i in range(num_of_lockers):
		lockers.append(1)


	while people_counter <= num_of_people:


		for locker_num in range(len(lockers)):

			for num in range(-1, len(lockers), people_counter+1):
				if lockers[num] == 0:
					lockers[num] = 1
				else:
					lockers[num] = 0

			people_counter+=1 


	for i in range(len(lockers)):
		if lockers[i] == 0:
			print 'Locker: ', i+1, ' is open.'
	
	return lockers


print locker_business(100, 100)