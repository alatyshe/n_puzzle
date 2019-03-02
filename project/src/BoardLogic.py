#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import copy

class BoardLogic():
	def __init__(self, board, size):
		pass

	@staticmethod
	def create_puzzle(size):
		'''
			Creates 1d array N x N in spiral order.
		'''
		final_arr = [[0 for x in range(size)] for y in range(size)]

		dir_y, dir_x = 0, 1
		y, x = 0, 0
		for i in range(1, size * size):
			if (x >= size-1 and dir_x == 1)\
					or (dir_x == 1 and final_arr[y][x+1] != 0):
				dir_y = 1
				dir_x = 0
			elif (y >= size-1 and dir_y == 1)\
					or (dir_y == 1 and final_arr[y+1][x] != 0):
				dir_y = 0
				dir_x = -1
			elif (x == 0 and dir_x == -1)\
					or (dir_x == -1 and final_arr[y][x-1] != 0):
				dir_y = -1
				dir_x = 0
			elif (y == 0 and dir_y == -1)\
					or (dir_y == -1 and final_arr[y-1][x] != 0):
				dir_y = 0
				dir_x = 1

			final_arr[y][x] = i
			y += dir_y
			x += dir_x

		final_arr = sum(final_arr, [])
		return final_arr

	@staticmethod
	def check_move(board, move, size):
		# board = 1d array
		empty_index = board.index(0)

		y = empty_index // size
		x = empty_index % size
		if move == "w" and y - 1 >= 0:
			return True
		elif move == "s" and y + 1 < size:
			return True
		elif move == "a" and x - 1 >= 0:
			return True
		elif move == "d" and x + 1 < size:
			return True
		return False


	@staticmethod
	def make_move(board, move, size):
		# board = 1d array
		empty_index = board.index(0)

		y = empty_index // size
		x = empty_index % size
		if move == "w":
			board[y * size + x] = board[(y - 1) * size + x]
			board[(y - 1) * size + x] = 0
		elif move == "s":
			board[y * size + x] = board[(y + 1) * size + x]
			board[(y + 1) * size + x] = 0
		elif move == "a":
			board[y * size + x] = board[y * size + x - 1]
			board[y * size + x - 1] = 0
		elif move == "d":
			board[y * size + x] = board[y * size + x + 1]
			board[y * size + x + 1] = 0

	@staticmethod
	def finished(board_input, board_final):
		return board_input == board_final;



