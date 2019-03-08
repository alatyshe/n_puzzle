# !/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os
import json
import queue as Q


from pprint import pprint
from algorithm.AStar import AStar

from src.BoardLogic import BoardLogic
from src.Node import Node
from src.Parser import Parser
from src.PuzzleGen import PuzzleGen

from metrics.HammingDistance import HammingDistance
from metrics.LinearConflicts import LinearConflicts
from metrics.ManhattanDistance import ManhattanDistance


if __name__ == "__main__":
  try:
    if not argv[1] and not os.path.isfile(argv[1]):
      parser = argparse.ArgumentParser()
      parser.add_argument("-size", type=int, default=3, help="Size of the puzzle's side. Must be >3.")
      parser.add_argument("-s", "-solvable", action="store_true", default=False, help="Forces generation of a solvable puzzle. Overrides -u.")
      parser.add_argument("-u", "-unsolvable", action="store_true", default=False, help="Forces generation of an unsolvable puzzle")
      parser.add_argument("-m", "-metric", type=int, default=1, help="\t0 = HammingDistance\n\t1 = ManhattanDistance\n\t2 = ManhattanDistance + LinearConflicts")
      args = parser.parse_args()

      if args.solvable and args.unsolvable:
        print ("Can't be both solvable AND unsolvable")
        sys.exit(1)
      elif args.solvable:
        board, size = PuzzleGen.generate(args.size, True)
      elif args.unsolvable:
        board, size = PuzzleGen.generate(args.size, False)
    else:
      file = open(sys.argv[1], "r")
      puzzle_string = file.read()
      board, size = Parser.parse_string(puzzle_string)


    Parser.check_invariant(board, size)

    metrics = [
      [HammingDistance],
      [ManhattanDistance(board["final_state"], board["size"])],
      [ManhattanDistance(board["final_state"], board["size"]), LinearConflicts]
    ]

    algorithm = AStar(
          metrics=metrics[metric_code],
          start_state=board["state"], 
          final_state=board["final_state"], 
          size=board["size"])

    result = algorithm.search()
    pprint(result)

    with open('../visual/app/db.txt', 'w') as f:
    	db = {}
    	db['size'] = board['size']
    	db['state'] = board["state"]
    	db['commands'] = []
    	for i in range(1, result["Move_num"] + 1):
    	  if result["Path"][-i][0]:
    	    db['commands'].append(result["Path"][-i][0].strip())
    	json.dump(db, f)
  except Exception as error:
    print(error)