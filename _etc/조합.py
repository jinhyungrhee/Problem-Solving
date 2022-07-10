# 조합(Combination) : nCr
# 서로 다른 n개 중에 r개를 선택하는 경우의 수 (순서 상관X)
# nCr = n! / (n-r)! * r!

# [방법1] : math.factiorial 사용

import sys, math

n, r = map(int, sys.stdin.readline().split())

n_C_r = math.factorial(n) // (math.factorial(n - r) * math.factorial(r))

print(n_C_r)

# [방법2] : itertools.combinations 사용

import sys
from itertools import combinations

n, r = map(int, sys.stdin.readline().split())

nums = [i for i in range(1, n+1)]
n_C_r = list(combinations(nums, r))

print('경우의 수 : %d개' % len(n_C_r))
print(n_C_r)


# ============================================================================

## 중복 조합 : nHr
## 중복 가능한 n개 중에서 r개를 선택하는 경우의 수 (순서 상관X)
## nHr = n+r-1 C r = (r+(n-1))! / r! * (n-1)!

# [방법1] : math.factiorial 사용

import sys, math

n, r = map(int, sys.stdin.readline().split())

n_H_r = math.factorial(r+(n - 1)) // (math.factorial(r) * math.factorial(n - 1))

print(n_H_r)

# [방법2] : itertools.combinations_with_replacement 사용

import sys
from itertools import combinations_with_replacement

n, r = map(int, sys.stdin.readline().split())

nums = [i for i in range(1, n+1)]
n_H_r = list(combinations_with_replacement(nums, 2))

print('경우의 수 : %d개' % len(n_H_r))
print(n_H_r)