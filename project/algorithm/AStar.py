#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import queue as Q

sys.path.append('..')
from src import Info, Node, BoardLogic

class AStar():
	def __init__(self, metric, start_state, size):
		# function
		self.metric = metric


		# 1d array
		print(start_state)
		self.start_state = start_state
		self.final_state = BoardLogic.create_puzzle(size)
		self.size = size

		# dict string_board : Node
		self.all_nodes = {}

		# A priority queue tuple
		self.open_nodes = {}

		self.closed_nodes = {}

	def search(self):
		
		open_nodes = {}
		# 
		closed_nodes = {}

	# 	open_nodes.append(start_node)
	# 	moves = ["up", "down", "left", "right"]


	# 	while len(open_nodes) != 0:
	# 		min_value_board = min(open_nodes, key=open_nodes.get)

	# 		for move in moves:
	# 			if logic.check_move():
	# 				new_node = Node(min_value_board, move, )
	# 				# open_nodes[]
