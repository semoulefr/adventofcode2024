# encoding: utf-8
# adventofcode 2024 02

## Functions
def check(report):
  # returns 0 if safe, else 1.
  prev = report[0]
  direction = 0  # 0 = unset, 1 = up, 2 = down

  for i in report[1:]:
    if abs(i-prev) > 3 or abs(i-prev) < 1:
      return 1
    if direction == 0:
      if i > prev:
        direction = 1
      else:
        direction = 2
    if i > prev and direction == 2:
      return 1
    if i < prev and direction == 1:
      return 1
    prev = i
  return(0)

def retry(report):
  # returns 0 if safe solution exists, else 1.
  for i in range(len(report)):
    report_candidate = report[:i] + report[i+1:]
    result = check(report_candidate)
    if result == 0:
      return(0)
  return 1

## Main
# load inputs
filepath = "input.txt"
reports = []
with open(filepath) as fp:
  for line in fp:
    lst_int = [int(x) for x in line.split()]
    reports.append(lst_int)

safe_count_part1 = 0
safe_count_part2 = 0
for report in reports:
  result = check(report)
  if result == 0:
    safe_count_part1 += 1
    safe_count_part2 += 1
  else:
    result = retry(report)
    if result == 0:
      safe_count_part2 += 1

# solution part1
print("solution part 1, safe reports:", safe_count_part1)
# solution part2
print("solution part 1, safe reports:", safe_count_part2)