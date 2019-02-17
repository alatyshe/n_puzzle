#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

sys.path.append('..')
from src import Info, Node, Board

class AStar():
	def __init__(self, start_node, logic_game, edge):
		self.start_node = start_node
		self.logic = logic_game
		self.edge = edge

	# def search(self, start_node):
	# 	open_nodes = {}
	# 	closed_nodes = {}

	# 	open_nodes.append(start_node)
	# 	moves = ["up", "down", "left", "right"]


	# 	while len(open_nodes) != 0:
	# 		min_value_board = min(open_nodes, key=open_nodes.get)

	# 		for move in moves:
	# 			if logic.check_move():
	# 				new_node = Node(min_value_board, move, )
	# 				# open_nodes[]
