# encoding: utf-8
# adventofcode 2024 04

def get_middle(update):
  return update[len(update) // 2]

def check_update(rules,update):
  total = 0
  res = 0
  for value in update:
    for rule in rules:
      pos0 = update.index(rule[0]) if rule[0] in update else None
      if pos0 != None:
        if rule[1] in update[0:pos0]:
          res += 1
  if res == 0:  
    total = get_middle(update)
  return total

def check_updates(rules,updates):
  total = 0
  for update in updates:
    total += check_update(rules,update)
  return total

# load inputs
filepath = "input.txt"
rules = []
updates = []
with open(filepath) as fp:
  for line in fp:
    if '|' in line: 
      rules.append(tuple(map(int, line.strip().split('|'))))
    elif ',' in line:
      updates.append(list(map(int, line.strip().split(','))))

total = check_updates(rules,updates)
print("solution part 1, total:", total)