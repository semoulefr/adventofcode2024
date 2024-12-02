# encoding: utf-8
# adventofcode 2024 01

# load inputs
filepath = "input.txt"
leftlist = []
rightlist = []
with open(filepath) as fp:
  for line in fp:
    leftlist.append(int(line.split()[0]))
    rightlist.append(int(line.split()[1]))

leftlist.sort()
rightlist.sort()

distlist = []
simlist = []
for i in range(len(leftlist)):
  # for part 1
  dist = abs(leftlist[i] - rightlist[i])
  distlist.append(dist)
  # for part 2
  sim = leftlist[i] * rightlist.count(leftlist[i])
  simlist.append(sim)

# solution part1
print("solution part 1, total distance:", sum(distlist))
# solution part2
print("solution part 2, similarity score:", sum(simlist))