#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import copy

class Board():
	def __init__(self, board, size):
		pass

	@staticmethod
	def check_move(board, move, size):
		empty_index = board.index(0)

		print("move : ", move)
		y = empty_index // size
		x = empty_index % size
		if move == "up" and y - 1 >= 0:
			return True
		elif move == "down" and y + 1 < size:
			return True
		elif move == "left" and x - 1 >= 0:
			return True
		elif move == "right" and x + 1 < size:
			return True
		return False


	@staticmethod
	def make_move(board, move, size):
		empty_index = board.index(0)

		y = empty_index // size
		x = empty_index % size
		if move == "up":
			board[y * size + x] = board[(y - 1) * size + x]
			board[(y - 1) * size + x] = 0
		elif move == "down":
			board[y * size + x] = board[(y + 1) * size + x]
			board[(y + 1) * size + x] = 0
		elif move == "left":
			board[y * size + x] = board[y * size + x - 1]
			board[y * size + x - 1] = 0
		elif move == "right":
			board[y * size + x] = board[y * size + x + 1]
			board[y * size + x + 1] = 0

	@staticmethod
	def finished(board):
		board_buff = copy.copy(board)

		# board_buff.remove(0)
		return False
		# return all(board_buff[i] <= board_buff[i+1] for i in range(len(board_buff)-1))



