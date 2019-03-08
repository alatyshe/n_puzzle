#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import array
from pprint import pprint


conflicts = []

# Get all linear conflicts in our board
# https://algorithmsinsight.wordpress.com/graph-theory-2/a-star-in-general/implementing-a-star-to-solve-n-puzzle/
def LinearConflicts(curr_state, final_state, size):
	global conflicts

	map = LinearMap(curr_state, final_state, size)

	for i in range(size ** 2):
		if curr_state[i] != final_state[i]:
			conflict(map=map, tail=curr_state[i], size=size)

	# print(set(conflicts))
	result = len(set(conflicts)) * 2
	conflicts = []
	return result

def LinearMap(curr_state, final_state, size):
	map = {}

	for i in range(size**2):
		map[curr_state[i]] = {'current': {'row': [], 'col': []}, 'final': {'row': [], 'col': []}}
		for j in range(size):
			map[curr_state[i]]['current']['row'].append(curr_state[(i // size) * size + j])
			map[curr_state[i]]['current']['col'].append(curr_state[(i % size) + (size * j)])
			map[curr_state[i]]['final']['row'].append(final_state[(i // size) * size + j])
			map[curr_state[i]]['final']['col'].append(final_state[(i % size) + (size * j)])
	return map

def conflict(map, tail, size):
	global conflicts

	col_diff = list(set(map[tail]['current']['col']) & set(map[tail]['final']['col'])) if tail in map[tail]['final']['col'] else []
	row_diff = list(set(map[tail]['current']['row']) & set(map[tail]['final']['row'])) if tail in map[tail]['final']['row'] else []

	current_col = map[tail]['current']['col']
	current_row = map[tail]['current']['row']

	final_col = map[tail]['final']['col']
	final_row = map[tail]['final']['row']

	# print(tail)
	if tail not in conflicts:
		for i, col in enumerate(col_diff):
			try:
				# print(col, col_diff[(i + 1) % size], 'current col:', current_col.index(col), ':', current_col.index(col_diff[(i + 1) % size]))
				# print(col, col_diff[(i + 1) % size], 'final col:', final_col.index(col), ':', final_col.index(col_diff[(i + 1) % size]))
				if (current_col.index(col) > current_col.index(col_diff[(i + 1) % size])\
					and final_col.index(col) < final_col.index(col_diff[(i + 1) % size]))\
					or (current_col.index(col) < current_col.index(col_diff[(i + 1) % size])\
					and final_col.index(col) > final_col.index(col_diff[(i + 1) % size])):
					conflicts += [col, col_diff[(i + 1) % size]]
			except IndexError:
				pass

	if tail not in conflicts:
		for i, row in enumerate(row_diff):
			try:
				# print(row, row_diff[(i + 1) % size], 'current row:', current_row.index(row), ':', current_row.index(row_diff[(i + 1) % size]))
				# print(row, row_diff[(i + 1) % size], 'final row:', final_row.index(row), ':', final_row.index(row_diff[(i + 1) % size]))
				if (current_row.index(row) > current_row.index(row_diff[(i + 1) % size])\
					and final_row.index(row) < final_row.index(row_diff[(i + 1) % size]))\
					or (current_row.index(row) < current_row.index(row_diff[(i + 1) % size])\
					and final_row.index(row) > final_row.index(row_diff[(i + 1) % size])):
					conflicts += [row, row_diff[(i + 1) % size]]
			except IndexError:
				pass


if __name__ == '__main__':
	# 3	2 1		1 2 3
	# 7 0 6		8 0 4
	# 8 4 5		7 6 5

	# curr = [3, 2, 1, 7, 0, 6, 8, 4, 5]
	# final = [1, 2, 3, 8, 0, 4, 7, 6, 5]

	#  1  4  3 2    1  2  3  4
	#  5  6 12 8   12 13 14  5
	#  9 10 11 7   11  0 15  6
	# 13 14 15 0   10  9  8  7

	curr = [1, 4, 3, 2, 5, 6, 12, 8, 9, 10, 11, 7, 13, 14, 15, 0]
	final = [1, 2, 3, 4, 12, 13, 14, 5, 11, 0, 15, 6, 10, 9, 8, 7]

	# 1 2 3		1 2 3
	# 7 0 4		8 0 4
	# 8 6 5		7 6 5

	# curr = [1, 2, 3, 7, 0, 4, 8, 6, 5]
	# final = [1, 2, 3, 8, 0, 4, 7, 6, 5]

	# pprint(LinearMap(curr, final, 4))
	print(LinearConflicts(curr, final, 4))
	# conflict(curr, final, 3)
