# 맞았지만 속도 너무 느림 -> 개선 방안 생각해보기
from itertools import combinations, permutations

n = int(input())

total_min = 987654321

teams = []
for i in range(1, n+1):
  teams.append(i)

grid = [
  list(map(int, input().split()))
  for _ in range(n)
]

combs = [0] + list(combinations(teams, n//2))

for i in range(1, len(combs)//2 + 1):
  p1 = list(permutations(combs[i], 2))
  p2 = list(permutations(combs[-i], 2))
  p1_sum = 0
  p2_sum = 0
  for coord in p1:
    a, b = coord
    p1_sum += grid[a-1][b-1]
  for coord in p2:
    c, d = coord
    p2_sum += grid[c-1][d-1]
  total_min = min(total_min, abs(p1_sum - p2_sum))

print(total_min)