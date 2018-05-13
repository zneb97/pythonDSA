from linkedList import linkedList

class Queue():

	def __init__(self):
		self.size = 0
		self.ll = linkedList()

	def getsize(self):
		return self.size

	def push(self, value):
		self.size += 1
		return self.ll.add(value)

	def pop(self):
		self.size -= 1
		return self.ll.remove(0)

	def isEmpty(self):
		return self.size == 0

	def peek(self):
		if not self.isEmpty:
			return self.ll.get(0)
		else:
			return None

	def toString(self):
		self.ll.toString()

class Stack():

	def __init__(self):
		self.size = 0
		self.ll = linkedList()

	def getsize(self):
		return self.size

	def push(self, value):
		self.size += 1
		return self.ll.add(value)

	def pop(self):
		self.size -= 1
		return self.ll.remove()

	def isEmpty(self):
		return self.size == 0

	def peek(self):
		if not self.isEmpty:
			return self.ll.get(0)
		else:
			return None

	def toString(self):
		self.ll.toString()