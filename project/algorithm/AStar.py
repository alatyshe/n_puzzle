#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import queue as Q

sys.path.append('..')
from src import Info, Node, BoardLogic

class AStar():
	def __init__(self, metric, start_state, final_state, size):
		# function
		self.metric = metric

		# 1d int array
		self.final_state = final_state
		self.final_state_string = ' '.join(str(i) for i in final_state)
		# board size - int
		self.size = size

		# dict string_state : Node
		self.all_nodes = {}
		self.closed_nodes = {}

		# A priority queue tuple (value, Node)
		self.open_nodes = Q.PriorityQueue()

		self.curr_node = Node(
				parent_state=[],
				current_state=start_state,
				num_move=0,
				metric_value=self.metric(start_state, self.final_state, self.size)
				)

		

	def search(self):
		moves = ["UP", "DOWN", "LEFT", "RIGHT"]

		self.open_nodes.put((self.curr_node.getF(), self.curr_node.getStateString()))
		self.all_nodes[self.curr_node.getStateString()] = self.curr_node

		while not self.open_nodes.empty():
			# Node
			self.curr_node = self.all_nodes[self.open_nodes.get()[1]]
			self.closed_nodes[self.curr_node.getStateString()] = self.curr_node

			print(self.curr_node.getStateString())
			if self.curr_node.getStateString() == self.final_state_string:
				break;

			for move in moves:
				if BoardLogic.check_move(self.curr_node.getState(), move, self.size):
					next_state = BoardLogic.make_move(self.curr_node.getState(), move, self.size)
					next_state_string = ' '.join(str(i) for i in next_state)
					if next_state_string not in self.closed_nodes:
						metric_value = self.metric(self.curr_node.getState(), self.final_state, self.size)

						new_node = Node(
								parent_state=self.curr_node.getState(),
								current_state=next_state,
								num_move=self.curr_node.getG() + 1,
								metric_value=self.metric(self.curr_node.getState(), self.final_state, self.size)
								)
						self.all_nodes[new_node.getStateString()] = new_node
						self.open_nodes.put((new_node.getF(), new_node.getStateString()))
			# print("closed_nodes : \n", self.closed_nodes)
			# print("all_nodes : \n", self.all_nodes)
			# print("\n\n\n")

		path = []
		while self.curr_node.getParentString() != "":
			path.append(self.curr_node)
			self.curr_node = self.all_nodes[self.curr_node.getParentString()]





	# 	open_nodes.append(start_node)
	# 	moves = ["up", "down", "left", "right"]


		# while True:
			# if 

	# 		min_value_board = min(open_nodes, key=open_nodes.get)

	# 		for move in moves:
	# 			if logic.check_move():
	# 				new_node = Node(min_value_board, move, )
	# 				# open_nodes[]
