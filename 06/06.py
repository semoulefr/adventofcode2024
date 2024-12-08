# encoding: utf-8
# adventofcode 2024 06

## functions
def move(lines, x, y, d, steps):
  out = False
  if d == "up":
    x, y, d, out, steps = moveup(lines, x, y, steps)
  elif d == "down":
    x, y, d, out, steps = movedown(lines, x, y, steps)
  elif d == "left":
    x, y, d, out, steps = moveleft(lines, x, y, steps)
  else:
    x, y, d, out, steps = moveright(lines, x, y, steps)
  return(x, y, d, out, steps)

def moveup(lines, x, y, steps):
  out = False
  d = "up"
  if y-1 < 0:
    out = True
  elif lines[y-1][x] != '#':
    y -= 1
    steps += 1
    visited.append((x,y))
  else:
    d = "right"
  return(x, y, d, out, steps)

def movedown(lines, x, y, steps):
  out = False
  d = "down"
  if y+1 >= len(lines):
    out = True
  elif lines[y+1][x] != '#':
    y += 1
    steps += 1
    visited.append((x,y))
  else:
    d = "left"
  return(x, y, d, out, steps)

def moveleft(lines, x, y, steps):
  out = False
  d = "left"
  if x-1 < 0:
    out = True
  elif lines[y][x-1] != '#':
    x -= 1
    steps += 1
    visited.append((x,y))
  else:
    d = "up"
  return(x, y, d, out, steps)

def moveright(lines, x, y, steps):
  out = False
  d = "right"
  if x+1 >= len(lines[0]):
    out = True
  elif lines[y][x+1] != '#':
    x += 1
    steps += 1
    visited.append((x,y))
  else:
    d = "down"
  return(x, y, d, out, steps)

def walk(lines, x, y, d):
  steps = 0
  out = False
  while not out:
    x, y, d, out, steps = move(lines, x, y, d, steps)
  return(steps)

def locate_guard(lines):
  y = 0
  for line in lines:
    if '^' in line:
      x = line.index('^')
      break
    y += 1
  return(x,y,"up")


## main
# load inputs
filepath = "sample.txt"
lines = []
with open(filepath) as fp:
  for line in fp:
    lines.append(line.strip())

# locate guard
x,y,d = locate_guard(lines)

visited = []
steps = walk(lines,x,y,d)
total = len(set(visited))
print("solution part 1, total:", total, "steps:", steps)