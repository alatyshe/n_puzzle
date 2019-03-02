#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import array
from src.BoardLogic import BoardLogic

# Calculate distance for single tile
# https://algorithmsinsight.wordpress.com/graph-theory-2/a-star-in-general/implementing-a-star-to-solve-n-puzzle/
def ManhattanScore(curr_state, size, finish_y, finish_x, y, x):

	calculate_state = [[0 for i in range(size)] for i in range(size)]
	
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


# Calculate distancescore for all board
# input: board and board_size
def ManhattanDistance(curr_state, final_state, size):
	total_score = 0
	# total tiles
	for i in range(size * size - 1):
		for j in range(len(curr_state)):
			if (curr_state[j] == i and curr_state[j] != final_state[j]):
				finish_y = (i - 1) // size
				finish_x = (i - 1) - finish_y * size
				y = (j - 1) // size
				x = (j - 1) - y * size
				total_score += ManhattanScore(curr_state, size, finish_y, finish_x, y, x)

	return total_score