# encoding: utf-8
# adventofcode 2024 06

## functions
def move(x, y, d, steps):
  out = False
  if d == "up":
    x, y, d, out, steps = moveup(x, y, steps)
  elif d == "down":
    x, y, d, out, steps = movedown(x, y, steps)
  elif d == "left":
    x, y, d, out, steps = moveleft(x, y, steps)
  else:
    x, y, d, out, steps = moveright(x, y, steps)
  return(x, y, d, out, steps)

def moveup(x, y, steps):
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

def movedown(x, y, steps):
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

def moveleft(x, y, steps):
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

def moveright(x, y, steps):
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

def walk(x, y, d):
  steps = 0
  out = False
  while not out:
    x, y, d, out, steps = move(x, y, d, steps)
  return(steps)

def locate_guard():
  y = 0
  for line in lines:
    if '^' in line:
      x = line.index('^')
      break
    y += 1
  return(x,y,"up")


## main
# load inputs
filepath = "input.txt"
lines = []
with open(filepath) as fp:
  for line in fp:
    lines.append(line.strip())

# locate guard
x,y,d = locate_guard()
visited = [(x,y)]

# let the guard walk until he left the map
steps = walk(x,y,d)

# get unique visited coordinates
total = len(set(visited))

print("solution part 1, total:", total, "steps:", steps)