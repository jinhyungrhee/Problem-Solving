import sys
from itertools import combinations_with_replacement

n, r = map(int, sys.stdin.readline().split())

nums = [i for i in range(1, n+1)]

n_H_r = list(combinations_with_replacement(nums, r)) # 중복 조합

for elem in n_H_r:
  print(*elem)

## 백트래킹 사용해서 다시 풀어보기! ** 