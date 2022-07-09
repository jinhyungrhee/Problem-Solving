from itertools import combinations
import sys

n, m = map(int, sys.stdin.readline().split())

nums = list(map(int, sys.stdin.readline().split()))

c_nums = list(combinations(nums, 3))

result = []
for c in c_nums:
  result.append(sum(c))

result.sort()

max_val = 0
for i in range(len(result)):
  if result[i] <= m:
    max_val = result[i]

print(max_val)