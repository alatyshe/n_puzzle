#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import array
from pprint import pprint


# from src.BoardLogic import BoardLogic


def GetElement(array, index):
	return array[index] if 0 <= index < len(array) else None


# def conflict(curr_state, final_state, index, size):
#     conflict = False
#
#     if (GetElement(curr_state, index + size) and GetElement(curr_state, index + size) == GetElement(final_state, index)
#         and GetElement(final_state, index + size)
#         and GetElement(final_state, index + size) == GetElement(curr_state, index)) \
#             or (GetElement(curr_state, index - size)
#                 and GetElement(curr_state, index - size) == GetElement(final_state, index)
#                 and GetElement(final_state, index - size)
#                 and GetElement(final_state, index - size) == GetElement(curr_state, index)):
#         conflict = True
#         print(GetElement(curr_state, index), GetElement(final_state, index))
#
#     return conflict


def LinearMap(curr_state, final_state, size):
	map = {}

	for i in range(size**2):
		map[i] = {curr_state[i]: {'current': {'row': [], 'col': []}, 'final': {'row': [], 'col': []}}}
		for j in range(size):
			map[i][curr_state[i]]['current']['row'].append(curr_state[(i // size) * size + j])
			map[i][curr_state[i]]['current']['col'].append(curr_state[(i % size) + (size * j)])
			map[i][curr_state[i]]['final']['row'].append(final_state[(i // size) * size + j])
			map[i][curr_state[i]]['final']['col'].append(final_state[(i % size) + (size * j)])
	return map


def conflict(state, size):
	pprint(state)


# Get all linear conflicts in our board
# https://algorithmsinsight.wordpress.com/graph-theory-2/a-star-in-general/implementing-a-star-to-solve-n-puzzle/
def LinearConflicts(curr_state, final_state, size):
	total_score = 0
	map = LinearMap(curr_state, final_state, size)

	for i in range(size ** 2):
		if curr_state[i] != final_state[i]:
			total_score += 1 if conflict(map[i], size) else 0

	return total_score


if __name__ == '__main__':
	# 3	2 1		1 2 3
	# 7 0 6		8 0 4
	# 8 4 5		7 6 5

	#  1  4  3 2    1  2  3  4
	#  5  6 12 8   12 13 14  5
	#  9 10 11 7   11  0 15  6
	# 13 14 15 0   10  9  8  7

	curr = [3, 2, 1, 7, 0, 6, 8, 4, 5]
	final = [1, 2, 3, 8, 0, 4, 7, 6, 5]
	print(LinearConflicts(curr, final, 3))
