#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import time
import queue as Q

sys.path.append('..')
from src import Node, BoardLogic

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

    # A priority queue tuple (value, string_state)
    # https://www.bogotobogo.com/python/python_PriorityQueue_heapq_Data_Structure.php
    self.open_nodes = Q.PriorityQueue()

    self.curr_node = Node(
        parent_state=[],
        current_state=start_state,
        num_move=0,
        move="",
        metric_value=self.metric(start_state, self.final_state, self.size)
        )

  def search(self):
    moves = ["UP", "DOWN", "LEFT", "RIGHT"]
    max_size = 1
    curr_size = 1

    self.open_nodes.put((self.curr_node.getF(), self.curr_node.getStateString()))
    self.all_nodes[self.curr_node.getStateString()] = self.curr_node

    start = time.time()
    while not self.open_nodes.empty():
      # Node
      self.curr_node = self.all_nodes[self.open_nodes.get()[1]]
      curr_size -= 1
      self.closed_nodes[self.curr_node.getStateString()] = self.curr_node

      if self.curr_node.getStateString() == self.final_state_string:
        break;

      for move in moves:
        if BoardLogic.check_move(self.curr_node.getState(), move, self.size):
          next_state = BoardLogic.make_move(self.curr_node.getState(), move, self.size)
          next_state_string = ' '.join(str(i) for i in next_state)
          if next_state_string not in self.all_nodes:
            new_node = Node(
                parent_state=self.curr_node.getState(),
                current_state=next_state,
                num_move=self.curr_node.getG() + 1,
                move=move,
                metric_value=self.metric(next_state, self.final_state, self.size)
                )
            self.all_nodes[new_node.getStateString()] = new_node
            self.open_nodes.put((new_node.getF(), new_node.getStateString()))
            curr_size += 1
            if max_size <= curr_size:
              max_size = curr_size

    path = []
    while self.curr_node.getMove() != "":
      path.append([self.curr_node.getMove(), self.curr_node.getStateString()])
      self.curr_node = self.all_nodes[self.curr_node.getParentString()]
    path.append([self.curr_node.getMove(), self.curr_node.getStateString()])

    res = {
      "Opened_nodes": len(self.all_nodes),
      "Max_states": max_size,
      "Path": path,
      "Move_num": len(path),
      "Time_spend": time.time() - start
    }
    return (res)
