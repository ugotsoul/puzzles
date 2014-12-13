#You are in a room with a circle of 100 chairs. The chairs are numbered sequentially from 1 to 100.
#At some point in time, the person in chair #1 will be asked to leave. The person in chair #2 will be skipped, and the person in chair #3 will be asked to leave. This pattern of skipping one person and asking the next to leave will keep going around the circle until there is one person left the survivor.
#Write a program to determine which chair the survivor is sitting in.

class Node:
	def __init__(self, initData):
		self.data = initData
		self.next = None

	def getData(self):
		return self.data

	def getNext(self):
		return self.next

class LinkedList:
	def __init__(self):
		self.head = None
		self.tail = None

	def append(self, item):
		tempNode = Node(item)
		
		if self.head:
			
			tempNode.next = self.head
			
			if self.tail:
				self.tail.next = tempNode
				self.tail = tempNode
			else:
				self.tail = tempNode
				self.head.next = self.tail

		else:
			self.head = tempNode

	def printList(self):

		currentNode = self.head

		for i in range(self.count()):
			print 'Current Node Data:',currentNode.data
			currentNode = currentNode.next
		return "end of list"

	def count(self):

		counter = 1
		currentNode = self.head

		while currentNode != self.tail:
			counter +=1
			currentNode = currentNode.next
		return counter

	#Note: returns the node object
	def find(self, data):
		currentNode = self.head

		for i in range(self.count()):
			if currentNode.data != data:
				currentNode = currentNode.next
			else:
				return currentNode

		return data, ": Data Not found"

	
	def delete(self, data):

		#find the node
		removeNode = self.find(data)

		#find the previous node
		
		refNode = self.head

		for i in range(self.count()):
			if removeNode.data != refNode.next.data:
				refNode = refNode.next

		print 'Reference Node:', refNode.data
		print 'Deletion node: ', refNode.next.data

		#change pointers
		if removeNode != self.tail:
			refNode.next = removeNode.next
			removeNode.next = None
		else:
			refNode.next = removeNode.next
			self.tail = refNode

		return refNode.next.data


def rude_chairs(num_of_chairs):

	chairs = LinkedList()

	for num in range(1, num_of_chairs+1):
		chairs.append(num)

	currentNode = chairs.head
	deleteNode = None

	while currentNode.next:
		pass


	

print rude_chairs(100)