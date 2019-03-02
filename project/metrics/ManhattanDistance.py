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
		for y in range(size):
			for x in range(size):
				if (curr_state[y][x] == i and curr_state[y][x] != final_state[y][x]):
					finish_y = (i - 1) // size
					finish_x = (i - 1) - finish_y * size
					total_score += ManhattanScore(curr_state, size, finish_y, finish_x, y, x)

	return total_score

# # final state of our board
# final_state = [
# 	[[1,   1], [2,  2], [3,   3], [4,  4],
	
# 	[[5,  12], [6, 13], [7,  14], [8,  5],

# 	[[9,  11], [10, 0], [11, 15], [12, 6],
	
# 	[[13, 10], [14, 9], [15,  8], [0,  7]]
# ]