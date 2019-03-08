#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import array
from pprint import pprint

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


def conflict(map, tail):
	col_diff = list(set(map[tail]['current']['col']) & set(map[tail]['final']['col']))
	row_diff = list(set(map[tail]['current']['row']) & set(map[tail]['final']['row']))

	# column = [
	# 	(e1, e2) for (e1, e2) in
	# 	zip([e for e in map[tail]['current']['col'] if e in map[tail]['final']['col']],
	# 		[e for e in map[tail]['final']['col'] if e in map[tail]['current']['col']])
	# 	# (e1, e2) for (e1, e2) in zip(map[tail]['current']['col'], map[tail]['final']['col'])
	# 	if e1 != e2 and (tail == e1 or tail == e2) and e1 in col_diff and e2 in col_diff
	# ]
	# row = [
	# 	(e1, e2) for (e1, e2) in
	# 	zip([e for e in map[tail]['current']['row'] if e in map[tail]['final']['row']],
	# 		[e for e in map[tail]['final']['row'] if e in map[tail]['current']['row']])
	# 	# (e1, e2) for (e1, e2) in zip(map[tail]['current']['row'], map[tail]['final']['row'])
	# 	if e1 != e2 and (tail == e1 or tail == e2) and e1 in row_diff and e2 in row_diff
	# ]

	# pprint(col_diff)
	# pprint(row_diff)
	# print(tail, ':', list(set(column) | set(row)))
	return 0


# Get all linear conflicts in our board
# https://algorithmsinsight.wordpress.com/graph-theory-2/a-star-in-general/implementing-a-star-to-solve-n-puzzle/
def LinearConflicts(curr_state, final_state, size):
	total_score = 0
	linear_map = LinearMap(curr_state, final_state, size)

	for i in range(size ** 2):
		if curr_state[i] != final_state[i]:
			total_score += conflict(map=linear_map, tail=curr_state[i])

	return total_score


if __name__ == '__main__':
	# 3	2 1		1 2 3
	# 7 0 6		8 0 4
	# 8 4 5		7 6 5

	curr = [3, 2, 1, 7, 0, 6, 8, 4, 5]
	final = [1, 2, 3, 8, 0, 4, 7, 6, 5]

	#  1  4  3 2    1  2  3  4
	#  5  6 12 8   12 13 14  5
	#  9 10 11 7   11  0 15  6
	# 13 14 15 0   10  9  8  7

	# curr = [1, 4, 3, 2, 5, 6, 12, 8, 9, 10, 11, 7, 13, 14, 15, 0]
	# final = [1, 2, 3, 4, 12, 13, 14, 5, 11, 0, 15, 6, 10, 9, 8, 7]

	# 1 2 3		1 2 3
	# 7 0 4		8 0 4
	# 8 6 5		7 6 5

	# curr = [1, 2, 3, 7, 0, 4, 8, 6, 5]
	# final = [1, 2, 3, 8, 0, 4, 7, 6, 5]

	# pprint(LinearMap(curr, final, 4))
	print(LinearConflicts(curr, final, 3))
