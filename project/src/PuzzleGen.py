#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random

from .BoardLogic import BoardLogic
from .Parser import Parser

class PuzzleGen(object):
  def __init__(self):
    pass


  @staticmethod
  def generate(size, solvable):
    while True:
      input_state = [i for i in range(size**2)]
      random.shuffle(input_state)
      
      final_state = BoardLogic.create_puzzle(size)
      inversions = Parser.inversions(input_state, size)
      inversions += Parser.inversions(final_state, size)
      if size % 2 == 0:
        inversions += final_state.index(0) // size
        inversions += input_state.index(0) // size
      if inversions % 2 != 0 and not solvable:
        return {"size" : size, 
              "state" : input_state,
              "final_state" : BoardLogic.create_puzzle(size)}
      elif inversions % 2 == 0 and solvable:
        return {"size" : size, 
              "state" : input_state,
              "final_state" : BoardLogic.create_puzzle(size)}
