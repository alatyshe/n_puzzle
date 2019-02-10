import sys
import array
# import numpy as np
import Board

# Информация про ноду 
# Хранит в себе состояние
#

# Расчет расстояния для конкретной плитки
def ManhattanScore(curr_state, size, finish_y, finish_x, y, x):
	calculate_state = [
			[0,0,0,0],
			[0,0,0,0],
			[0,0,0,0],
			[0,0,0,0]
	]
	calculate_state[finish_y][finish_x] = 1
	while calculate_state[y][x] == 0:
		for y in range(size):
			for x in range(size):
				if calculate_state[y][x] != 0:
					if (y + 1 < size and calculate_state[y + 1][x] == 0):
						calculate_state[y + 1][x] = calculate_state[y][x] + 1;
					if (y - 1 >= 0 and calculate_state[y - 1][x] == 0):
						calculate_state[y - 1][x] = calculate_state[y][x] + 1;
					if (x + 1 < size and calculate_state[y][x + 1] == 0):
						calculate_state[y][x + 1] = calculate_state[y][x] + 1;
					if (x - 1 >= 0 and calculate_state[y][x - 1] == 0):
						calculate_state[y][x - 1] = calculate_state[y][x] + 1;
	return calculate_state[finish_y][finish_x]



# https://algorithmsinsight.wordpress.com/graph-theory-2/a-star-in-general/implementing-a-star-to-solve-n-puzzle/
# передаем массив интов NxN:
# просто манхэттенское расстояние
def ManhattanDistance(curr_state, size):
	total_score = 0

	# Финальное сотояние доски поправить чтобы просто использовать size для генерации доски
	final_state = [
			[1, 2, 3, 4],
			[5, 6, 7, 8],
			[9,10,11,12],
			[13,14,15,0]
	]
	# количество наших плиток
	for i in range(size * size - 1):
		for y in range(size):
			for x in range(size):
				if (curr_state[y][x] == i and curr_state[y][x] != final_state[y][x]):
					finish_y = (i - 1) // size
					finish_x = (i - 1) - finish_y * size
					total_score += ManhattanScore(curr_state, size, finish_y, finish_x, y, x)


		

def Linear_Conflict_Manhattan_Distance(state):
	pass
	# манхэттенское расстояние + количество линейных конфликтов умноженных на 2





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
