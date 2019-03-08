#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Metrics
import metrics.ManhattanDistance
import metrics.LinearConflicts
import metrics.HammingDistance

class Node():
  def __init__(self, parent_state, current_state, num_move, move, metric_value):
    # distance from start node(total number of moves)
    self.g_cost = num_move
    # our metric
    self.h_cost = metric_value
    # Total value
    self.f_cost = self.g_cost + self.h_cost

    self.move = move

    self.parent_state_string = ' '.join(str(i) for i in parent_state)

    self.current_state = current_state
    self.current_state_string = ' '.join(str(i) for i in current_state)

  def __cmp__(self, other):
    return cmp(self.f_cost, other.getF())

  def getF(self):
    return self.f_cost

  def getG(self):
    return self.g_cost

  def getH(self):
    return self.h_cost
  
  def getMove(self):
    return self.move

  def getState(self):
    return self.current_state

  def getStateString(self):
    return self.current_state_string

  def getParentString(self):
    return self.parent_state_string
