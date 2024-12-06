# encoding: utf-8
# adventofcode 2024 02

import re

## Functions
def extract_compute(line):
  total = 0
  extracted = re.findall(r"mul\((\d{1,3}),(\d{1,3})\)", line)
  for e in extracted:
    total += int(e[0])*int(e[1])
  return(total)

## Main
# load inputs
filepath = "input.txt"
memory = ""
with open(filepath) as fp:
  memory = fp.read()

# part 1
total = extract_compute(memory)
print("solution part 1, total:", total)

# part 2
total = 0
parts = memory.split("do()")
for part in parts:
  truncated = part.split("don't()")[0]
  total += extract_compute(truncated)

print("solution part 2, total:", total)