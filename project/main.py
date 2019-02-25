# !/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import numpy

from algorithm.AStar import AStar

from src.Board import Board
from src.Info import Info
from src.Node import Node
from src.Parser import Parser

from metrics.HammingDistance import HammingDistance
from metrics.LinearConflicts import LinearConflicts
from metrics.ManhattanDistance import ManhattanDistance


if __name__ == "__main__":
	try:
		if len(sys.argv) > 1:
			file = open(sys.argv[1], "r")
			puzzle_string = file.read()

			board = Parser.parse_string(puzzle_string)

			# print(board)
			# n = board[0]
			# final_arr = [[x for x in range(n * y + 1,n * y + n + 1)] for y in range(n)]

			# print(final_arr)

		else :
			print("Usage:\n\tmain.py puzzle.txt")
	except Exception as error:
		print(error)



	# logic = Board(board[1], board[0])
	# a_board = board[1]
	# edge = board[0]
	# prompt_str = "choice move[up; down; left; right]: "
	# while not logic.finished(a_board):
	# 	for i in range(edge):
	# 		print (" | ".join('%02s' % i for i in a_board[i * edge : (i + 1) * edge]))
	# 		print ("- " * ((edge + 1) * 2))


	# 	move = input(prompt_str)

	# 	if logic.check_move(a_board, move, edge):
	# 		logic.make_move(a_board, move, edge)
	# 		prompt_str = "choice move[up; down; left; right]: "
	# 	else:
	# 		prompt_str = "invalid move [" + move + "] try again : "

		
	# node = Node.Node(None)
	# info = Info.Info()
	# algorithm = AStar()

