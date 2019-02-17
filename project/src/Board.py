#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import copy

class Board():
	def __init__(self):
		pass

	@staticmethod
	def invariant(board, edge):
		board_buff = copy.copy(board)

		board_buff.remove(0)

		return True


	@staticmethod
	def check_move(board, move, edge):
		empty_index = board.index(0)

		print("move : ", move)
		y = empty_index // edge
		x = empty_index % edge
		if move == "up" and y - 1 >= 0:
			return True
		elif move == "down" and y + 1 < edge:
			return True
		elif move == "left" and x - 1 >= 0:
			return True
		elif move == "right" and x + 1 < edge:
			return True
		return False


	@staticmethod
	def make_move(board, move, edge):
		empty_index = board.index(0)

		y = empty_index // edge
		x = empty_index % edge
		if move == "up":
			board[y * edge + x] = board[(y - 1) * edge + x]
			board[(y - 1) * edge + x] = 0
		elif move == "down":
			board[y * edge + x] = board[(y + 1) * edge + x]
			board[(y + 1) * edge + x] = 0
		elif move == "left":
			board[y * edge + x] = board[y * edge + x - 1]
			board[y * edge + x - 1] = 0
		elif move == "right":
			board[y * edge + x] = board[y * edge + x + 1]
			board[y * edge + x + 1] = 0

	@staticmethod
	def finished(board):
		board_buff = copy.copy(board)

		board_buff.remove(0)
		return all(board_buff[i] <= board_buff[i+1] for i in range(len(board_buff)-1))



