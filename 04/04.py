# encoding: utf-8
# adventofcode 2024 04

import re

# functions
def count_horizontal(puzzle):
  total = 0
  for line in puzzle:
    total += line.count("XMAS")
    total += line.count("SAMX")
  return total

def count_vertical(puzzle):
  total = 0
  puzzle_width = len(puzzle[0])
  puzzle_length = len(puzzle)
  for i in range(puzzle_width - 3):
    for j in range(puzzle_length):
      if puzzle[i][j] == "X" and puzzle[i+1][j] == "M" and puzzle[i+2][j] == "A" and puzzle[i+3][j] == "S":
        total += 1
      if puzzle[i][j] == "S" and puzzle[i+1][j] == "A" and puzzle[i+2][j] == "M" and puzzle[i+3][j] == "X":
        total += 1
  return total

def count_diagonal(puzzle):
  total = 0
  puzzle_width = len(puzzle[0])
  puzzle_length = len(puzzle)
  # diagonal to right
  for i in range(puzzle_width - 3):
    for j in range(puzzle_length - 3):
      if puzzle[i][j] == "X" and puzzle[i+1][j+1] == "M" and puzzle[i+2][j+2] == "A" and puzzle[i+3][j+3] == "S":
        total += 1
      if puzzle[i][j] == "S" and puzzle[i+1][j+1] == "A" and puzzle[i+2][j+2] == "M" and puzzle[i+3][j+3] == "X":
        total += 1
  return total

def mirror(puzzle):
  puzzle_mirror = []
  for line in puzzle:
    puzzle_mirror.append(line[::-1])
  return(puzzle_mirror)

# main
# load inputs
filepath = "input.txt"
puzzle = []
with open(filepath) as fp:
  for line in fp:
    puzzle.append(line.strip())

total = 0
total += count_vertical(puzzle)
total += count_horizontal(puzzle)
total += count_diagonal(puzzle)
total += count_diagonal(mirror(puzzle))

print("solution part 1, total:", total)
