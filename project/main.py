# !/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import queue as Q
# import numpy

from algorithm.AStar import AStar

from src.BoardLogic import BoardLogic
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

			algorithm = AStar(
						metric=HammingDistance, 
						start_state=board["state"], 
						final_state=board["final_state"], 
						size=board["size"])

			result = algorithm.search()
			print(result)
		else :
			print("Usage:\n\tmain.py puzzle.txt")
	except Exception as error:
		print(error)



	# logic = Board(board[1], board[0])

	# logic = Board(board, 3)
	# edge = board[0]
	# prompt_str = "choice move[w; s; a; d]: "
	# while not logic.finished(board):
	# 	for i in range(edge):
	# 		print (" | ".join('%02s' % i for i in board[i * edge : (i + 1) * edge]))
	# 		print ("- " * ((edge + 1) * 2))


	# 	move = input(prompt_str)

	# 	if logic.check_move(board, move, edge):
	# 		logic.make_move(board, move, edge)
	# 		prompt_str = "choice move[up; down; left; right]: "
	# 	else:
	# 		prompt_str = "invalid move [" + move + "] try again : "

		
	# node = Node.Node(None)
	# info = Info.Info()
	# algorithm = AStar()

