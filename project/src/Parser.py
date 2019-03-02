#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import copy
from .BoardLogic import BoardLogic

def getIndex( matrix, digit ):
		for row, j in enumerate( matrix ):
				for column,l in enumerate( j ):
						if l == digit:
								return row
def inversion( State ):
		lst_goal = []
		lst = []
		for row, j in enumerate( State ):
				for column, l in enumerate( j ):
						if l == 0:
								pass
						else:
								lst.append(l)
		for row, j in enumerate( State ):
				for column, l in enumerate(j):
						if l == 0:
								pass
						else:
								lst_goal.append(l)
		inv_count = 0
		for comp in lst_goal:
				del lst[0]
				for itera in lst:
						if (comp > itera):
								inv_count += 1
		return inv_count
def isSolvable( startState, goalState ):
		size = len(startState)
		inv = 0
		inv += inversion( startState )
		inv += inversion( goalState )
		if size % 2 == 0:
				inv += getIndex(startState, 0)
				inv += getIndex(goalState, 0)

		print("inv : ", inv)
		if not inv % 2 == 0:
				return False
		return True
# isSolvable(input_state, final_state)


class Parser(object):
	def __init__(self):
		pass
	
	@staticmethod
	def inversions(input_state, size):
		inversions = 0
		for i in range(size**2 - 1):
			for j in range(i + 1, size**2):
				if input_state[i] > input_state[j] and\
						input_state[i] != 0 and\
						input_state[j] != 0:
					inversions += 1

		return inversions

	@staticmethod
	def parse_string(string):
		size = -1
		# delete comments
		cropped_string = [i.split("#")[0] for i in string.split("\n") if len(i.split("#")[0]) > 0]

		if len(cropped_string) == 0:
			raise ValueError(f"Error, empty file")
		# check for numbers and spaces in string
		for string in cropped_string:
			if not all(char.isdigit() or char.isspace() for char in string):
				raise ValueError(f"Error, Invalid input(chars in line): {string}")

		# get numbers from string and write it in array
		parsed_numbers = [[int(num) for num in line.split()] for line in cropped_string]

		# if we havent normal size of our board
		if len(parsed_numbers[0]) != 1:
			raise ValueError(f"Error, Invalid board size: {cropped_string[0]}")

		size = parsed_numbers[0][0]
		input_state = parsed_numbers[1:]

		# check for sizes each line in our board
		for line in input_state:
			if len(line) != size:
				raise ValueError(f"Error, Invalid line: {' '.join(str(i) for i in line)}")

		# max value on board
		# for board 4x4, max num will be 15
		# for board 3x3 => 8
		board_max_num = size**2 - 1

		# check size and sum of numbers in board
		if sum(map(sum, input_state)) != (board_max_num**2 + board_max_num) / 2:
			raise ValueError(f"Error, Invalid board input")

		# Reshape to 1d array
		input_state = sum(input_state, [])

		# check for repeated numbers
		sorted_input = input_state.copy()
		sorted_input.sort()
		for i in range(board_max_num):
			if sorted_input[i] >= sorted_input[i+1]:
				raise ValueError(f"Error, Invalid line: repeated numbers")


		# check invariant
		# http://www.cs.bham.ac.uk/~mdr/teaching/modules04/java2/TilesSolvability.html
		final_state = BoardLogic.create_puzzle(size)
		inversions = Parser.inversions(input_state, size)
		if size % 2 == 0:
			inversions += Parser.inversions(final_state, size)
			inversions += final_state.index(0) // size
			inversions += input_state.index(0) // size
		if inversions % 2 != 0:
			raise ValueError(f"Error, Puzzle is unsolvable")	
		return {"size" : size, 
						"state" : input_state}

	
