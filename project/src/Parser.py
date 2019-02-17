#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import copy
# import numpy

class Parser(object):
	"""docstring for Parser"""
	def __init__(self):
		pass

	@staticmethod
	def parse_string(string):
		size = -1
		# delete comments
		cropped_string = [i.split("#")[0] for i in string.split("\n") if len(i.split("#")[0]) > 0]

		# check for numbers and spaces in string
		for string in cropped_string:
			if not all(char.isdigit() or char.isspace() for char in string):
				raise ValueError(f"Error, Invalid input(chars in line): {string}")

		# get numbers from string and write it in array
		parsed_numbers = [[int(num) for num in line.split()] for line in cropped_string]

		# if we havent normal size of our board
		if len(parsed_numbers[0]) != 1:
			raise ValueError(f"Error, Invalid board size: {cropped_string[0]}")

		board_size = parsed_numbers[0][0]
		board = parsed_numbers[1:]

		# check for sizes each line in our board
		for line in board:
			if len(line) != board_size:
				raise ValueError(f"Error, Invalid line: {' '.join(str(i) for i in line)}")

		# max value on board
		# for board 4x4, max num will be 15
		# for board 3x3 => 8
		board_max_num = board_size**2 - 1

		# check board_size and sum of numbers in board
		if sum(map(sum, board)) != (board_max_num**2 + board_max_num) / 2:
			raise ValueError(f"Error, Invalid board input")

		reshaped_board = sum(board, [])

		# check for repeated numbers
		sorted_reshaped_board = reshaped_board.copy()		
		sorted_reshaped_board.sort()
		for i in range(board_max_num):
			if sorted_reshaped_board[i] >= sorted_reshaped_board[i+1]:
				raise ValueError(f"Error, Invalid line: repeated numbers")


		# Not Working
		# # check invariant
		# # http://www.cs.bham.ac.uk/~mdr/teaching/modules04/java2/TilesSolvability.html
		# inversions = 0
		# for i in range(board_max_num):
		# 	for j in range(i + 1, board_max_num + 1):
		# 		print(f"{i} : {j}")
		# 		if reshaped_board[j] > reshaped_board[i] and\
		# 				reshaped_board[i] != 0 and\
		# 				reshaped_board[j] != 0:
		# 			print(f"\t\t{reshaped_board[j]} > {reshaped_board[i]}")
		# 			inversions += 1
		# if inversions%2 == 1:
		# 	raise ValueError(f"Error, Puzzle is unsolvable")

		# print(inversions)
		# print(reshaped_board)
		# print(reshaped_board[j])
		return [board_size, reshaped_board]

	
