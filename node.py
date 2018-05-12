#!/usr/bin/env python


"""
Benjamin Ziemann
benjamin.ziemann@students.olin.edu

Implementation of node class
"""

class Node():

	def __init__(self):
		self.key = None

		self.next = None
		self.prev = None

		self.parent = None
		self.child = None

		self.marked = False