#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import array
# import numpy as np
# from src.BoardLogic import BoardLogic

# Calculate distance for single tile
# https://algorithmsinsight.wordpress.com/graph-theory-2/a-star-in-general/implementing-a-star-to-solve-n-puzzle/
def ScoreForOneTile(in_y, in_x, size):
  dist_board = [[0 for i in range(size)] for i in range(size)]
  filled = False
  num = 1

  if (in_y + 1 < size):
    dist_board[in_y + 1][in_x] = 1;
  if (in_y - 1 >= 0):
    dist_board[in_y - 1][in_x] = 1;
  if (in_x + 1 < size):
    dist_board[in_y][in_x + 1] = 1;
  if (in_x - 1 >= 0):
    dist_board[in_y][in_x - 1] = 1;

  while not filled:
    filled = True
    for y in range(size):
      for x in range(size):
        if dist_board[y][x] == num:
          if (y + 1 < size and dist_board[y + 1][x] == 0):
            dist_board[y + 1][x] = dist_board[y][x] + 1;
            filled = False
          if (y - 1 >= 0 and dist_board[y - 1][x] == 0):
            dist_board[y - 1][x] = dist_board[y][x] + 1;
            filled = False
          if (x + 1 < size and dist_board[y][x + 1] == 0):
            dist_board[y][x + 1] = dist_board[y][x] + 1;
            filled = False
          if (x - 1 >= 0 and dist_board[y][x - 1] == 0):
            dist_board[y][x - 1] = dist_board[y][x] + 1;
            filled = False
    num += 1

  dist_board[in_y][in_x] = 0
  return sum(dist_board, [])


# Calculate distancescore for all board
# input: 1d array and int
def ManhattanDistance(final_state, size):
  # key : 1d array
  distance_map = {}

  for i in range(len(final_state)):
    y = i // size
    x = i - y * size
    distance_map[final_state[i]] = ScoreForOneTile(y, x, size)


  # b = np.reshape(final_state, (-1, size))
  # print("FINAL MAP : ")
  # for i in b:
  #   print(i)

  # for i in distance_map:
  #   b = np.reshape(distance_map[i], (-1, size))
  #   print (i, " : ")
  #   for i in b:
  #     print(i)


  def CalculateScore(curr_state, final_state, size):
    total_score = 0

    for i in range(len(curr_state)):
      dist_board = distance_map[curr_state[i]]
      total_score += dist_board[i]
    return total_score

  return CalculateScore



