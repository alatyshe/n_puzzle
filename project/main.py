# !/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

from algorithm.AStar import AStar

from src.Board import Board
from src.Info import Info
from src.Node import Node

from metrics.HammingDistance import HammingDistance
from metrics.LinearConflicts import LinearConflicts
from metrics.ManhattanDistance import ManhattanDistance


edge = 5

if __name__ == "__main__":

	edge = 4
	a_board = [
		10,  6,  4,  8,
		2,  1,  7, 15,
		9, 11,  3, 12,
		13,  5,  0, 14]

	a_board = [
		1,  2,  3,  4,
		5,  6,  7, 8,
		9, 10,  0, 12,
		13,  14,  11, 15]



	logic = Board()

	prompt_str = "choice move[up; down; left; right]: "
	while not logic.finished(a_board):
		for i in range(edge):
			print (" | ".join('%02s' % i for i in a_board[i * edge : (i + 1) * edge]))
			print ("- " * ((edge + 1) * 2))


		move = input(prompt_str)

		if logic.check_move(a_board, move, edge):
			logic.make_move(a_board, move, edge)
			prompt_str = "choice move[up; down; left; right]: "
		else:
			prompt_str = "invalid move [" + move + "] try again : "

		
	# node = Node.Node(None)
	# info = Info.Info()
	algorithm = AStar.AStar()

