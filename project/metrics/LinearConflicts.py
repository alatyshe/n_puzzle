#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import array
from src.BoardLogic import BoardLogic

# Get all linear conflicts in our board
# https://algorithmsinsight.wordpress.com/graph-theory-2/a-star-in-general/implementing-a-star-to-solve-n-puzzle/
def LinearConflicts(curr_state, final_state, size):
	total_score = 0

	return total_score