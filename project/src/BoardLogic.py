#!/usr/bin/env python
# -*- coding: utf-8 -*-

import copy

class BoardLogic(object):
  def __init__():
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
  def check_move(current_state, move, size):
    # current_state = 1d array
    empty_index = current_state.index(0)

    y = empty_index // size
    x = empty_index % size
    if move == "UP" and y - 1 >= 0:
      return True
    elif move == "DOWN" and y + 1 < size:
      return True
    elif move == "LEFT" and x - 1 >= 0:
      return True
    elif move == "RIGHT" and x + 1 < size:
      return True
    return False


  @staticmethod
  def make_move(current_state, move, size):
    # current_state = 1d array
    next_state = current_state.copy()
    empty_index = next_state.index(0)

    y = empty_index // size
    x = empty_index % size
    if move == "UP":
      next_state[y * size + x] = next_state[(y - 1) * size + x]
      next_state[(y - 1) * size + x] = 0
    elif move == "DOWN":
      next_state[y * size + x] = next_state[(y + 1) * size + x]
      next_state[(y + 1) * size + x] = 0
    elif move == "LEFT":
      next_state[y * size + x] = next_state[y * size + x - 1]
      next_state[y * size + x - 1] = 0
    elif move == "RIGHT":
      next_state[y * size + x] = next_state[y * size + x + 1]
      next_state[y * size + x + 1] = 0
    return next_state

  @staticmethod
  def finished(current_state, final_state):
    return current_state == final_state;
