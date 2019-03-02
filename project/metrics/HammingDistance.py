#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import array
from src.BoardLogic import BoardLogic

# Just the total number of tiles that are in place
# https://algorithmsinsight.wordpress.com/graph-theory-2/a-star-in-general/implementing-a-star-to-solve-n-puzzle/
def HammingDistance(curr_state, final_state, size):
	total_score = 0
	for i in range(size * size - 1):
		for y in range(size):
			for x in range(size):
				if (curr_state[y][x] == i and curr_state[y][x] != final_state[y][x]):
					total_score += 1

	return total_score