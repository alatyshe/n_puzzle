# !/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import json
import queue as Q

from algorithm.AStar import AStar

from src.BoardLogic import BoardLogic
from src.Node import Node
from src.Parser import Parser

from metrics.HammingDistance import HammingDistance
from metrics.LinearConflicts import LinearConflicts
from metrics.ManhattanDistance import ManhattanDistance


if __name__ == "__main__":
  try:
    if len(sys.argv) > 1:
      file = open(sys.argv[1], "r")
      puzzle_string = file.read()

      board = Parser.parse_string(puzzle_string)

      # print("ManhattanDistance : ")
      # algorithm = AStar(
      #       metric=ManhattanDistance(board["final_state"], board["size"]), 
      #       start_state=board["state"], 
      #       final_state=board["final_state"], 
      #       size=board["size"])

      # result = algorithm.search()
      # print(result)

      print("HammingDistance : ")
      algorithm = AStar(
            metric=HammingDistance,
            start_state=board["state"], 
            final_state=board["final_state"], 
            size=board["size"])

      result = algorithm.search()
      print(result)

      # print("LinearConflicts : ")
      # algorithm = AStar(
      #       metric=LinearConflicts,
      #       start_state=board["state"], 
      #       final_state=board["final_state"], 
      #       size=board["size"])

      # result = algorithm.search()
      # print(result)

      with open('../visual/app/db.txt', 'w') as f:
      	db = {}
      	db['size'] = board['size']
      	db['state'] = board["state"]
      	db['commands'] = []
      	for i in range(1, result["Move_num"] + 1):
      	  if result["Path"][-i][0]:
      	    db['commands'].append(result["Path"][-i][0].strip())
      	json.dump(db, f)

    else :
      print("Usage:\n\tmain.py puzzle.txt")
  except Exception as error:
    print(error)