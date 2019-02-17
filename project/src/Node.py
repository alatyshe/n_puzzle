#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import array

# Metrics
import metrics.ManhattanDistance
import metrics.LinearConflicts
import metrics.HammingDistance

class Node():
	def __init__(self, parent, move, g, h, edge):
		# distance from start node
		self.g_cost = g
		# distance from end node
		self.h_cost = h

		self.edge 	= edge

		# доска родитель(просто строка).
		# Вся эта схема нужна для того, чтобы сформировать граф от конца к началу
		# создаем dict всех возможных состояний в таком виде
		# строка - ключ
		# Node - значение
		# {state: Node}
		self.parent = parent
		# текущее состояние доски(просто строка)
		self.state 	= copy.copy(parent, move, edge)


	def getF(self):
		pass

	def getG(self):
		return self.g

	def setG(self, g):
		self.g = g

	def getH(self):
		return self.h
		
	def setH(self, h):
		return self.h

	def getParent(self):
		return self.parent

	def setParent(self, parent):
		self.parent = parent

	def equals(self, state):
		return false
