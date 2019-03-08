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
      new_state = [i for i in range(size**2)]
      random.shuffle(new_state)
      
      final_state = BoardLogic.create_puzzle(size)
      inversions = Parser.inversions(new_state, size)
      inversions += Parser.inversions(final_state, size)
      if size % 2 == 0:
        inversions += final_state.index(0) // size
        inversions += new_state.index(0) // size
      if inversions % 2 != 0 and not solvable:
        return new_state, size
      elif inversions % 2 == 0 and solvable:
        return new_state, size
