from node import Node

class linkedList():

	def __init__(self):

		self.head = None
		self.tail = None
		self.size = 0

	def getSize(self):
		"""
		Returns the size of the linked list
		"""
		return self.size

	def isEmpty(self):
		"""
		Returns if the linked list is empty
		"""
		return self.size == 0

	def add(self, value, i=-1):
		"""
		Adds a new node to the list

		Value is some object
		i is the index to add to. 
		If no index is specified it is added to the end

		Returns the removed node
		"""
		newNode = Node()
		newNode.key = value

		if i == 0:
			return self.__addFirst(newNode)
		elif i == -1:
			return self.__addLast(newNode)
		else:
			return self.__addIndex(i, newNode)

	def __addLast(self, newNode):
		"""
		Adds the node to the end of the list

		Returns the added node
		"""
		if self.tail != None:
			self.tail.next = newNode
			newNode.prev = self.tail
			self.tail = newNode
		else:
			self.head = newNode
			self.tail = newNode

		self.size += 1
		return newNode.key

	def __addFirst(self, newNode):
		"""
		Adds a new node to the beginning of the list

		Returns the added node key
		"""

		if self.size == 0:
			self.head = newNode
			self.tail = newNode
		else:
			self.head.prev = newNode
			newNode.next = self.head
			self.head = newNode

		self.size += 1
		return newNode.key

	def __addIndex(self, i, newNode):
		"""
		Adds the node to a specified index

		Returns the added node key
		"""

		if i > self.size:
			raise ValueError("Index out of bounds")

		elif i == 0:
			self.size += 1
			return self.addFirst(newNode)

		elif i == self.size:
			self.size += 1
			return self.addLast(newNode)

		else:
			currNode = self.head
			for j in range(1,self.size):
				if j == i:
					newNode.next = currNode.next
					newNode.prev = currNode
					currNode.next.prev = newNode
					currNode.next = newNode
				else:
					currNode = currNode.next


			self.size += 1
			return newNode.key


	def remove(self, i=-1):
		"""
		Removes a specified index from the list

		i is the index to remove to. 
		If no index is specified it is removed to the end

		Returns the removed node
		"""
		if self.size == 0:
			raise ValueError("List already empty")

		if i == 0:
			return self.__removeFirst()
		elif i == -1:
			return self.__removeLast()
		else:
			return self.__removeIndex(i) 

	def __removeLast(self):
		"""
		Removes the node at the end of the list

		Returns the removed node
		"""
		temp = self.tail
		if self.size == 1:
			self.head = None
			self.tail = None

		else:
			self.tail.prev.next = None
			self.tail = self.tail.prev

		self.size -= 1
		return temp.key


	def __removeFirst(self):
		"""
		Removes the node at the start of the list

		Returns the removed node
		"""
		temp = self.head

		if self.size == 1:
			self.head = None
			self.tail = None
		else:
			self.head.next.prev = None
			self.head = self.head.next
		
		self.size -= 1
		return temp.key

	def __removeIndex(self, i):
		"""
		Removes the node at a specific of the list

		Returns the removed node
		"""
		if i > self.size:
			raise ValueError("Index out of bounds")

		elif i == 0:
			self.size -= 1
			return self.removeFirst()

		elif i == self.size:
			self.size -= 1
			return self.removeLast()

		else:
			currNode = self.head
			for j in range(0,self.size):
				if j == i:
					currNode.prev.next = currNode.next
					currNode.next.prev = currNode.prev
				else:
					currNode = currNode.next


			self.size -= 1
			return currNode.key



	def get(self, index):
		"""
		Returns the node at a specified index
		"""
		if index > self.size:
			raise ValueError('Index out of bounds')
		current = self.head
		for i in range(index):
			current = current.next
		return current

	def contains(self, value):
		"""
		Returns the index of the value if the key is in the list

		Returns -1 if not in the list
		"""
		currNode = self.head
		for i in range(self.size):
			if currNode.key == value:
				return i
			else:
				currNode = currNode.next
		return -1
		

	def toString(self):
		if self.size == 0:
			return

		current = self.head
		for i in range(self.size):
			print(current.key)
			current = current.next

