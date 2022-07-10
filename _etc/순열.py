# 순열(Permutation) : nPr
# 서로 다른 n개 중에 r개를 선택하는 경우의 수 (순서 상관 O)
# nPr = n! / (n - r)!

# [방법1] : math.factiorial 사용

import sys, math

n, r = map(int, sys.stdin.readline().split())

n_P_r = math.factorial(n) // math.factorial(n - r)

print(n_P_r)

# [방법2] : itertools.permutations 사용

import sys
from itertools import permutations

n, r = map(int, sys.stdin.readline().split())

nums = [i for i in range(1, n+1)]
n_P_r = list(permutations(nums, r))

print('경우의 수 : %d개' % len(n_P_r))
print(n_P_r)


# =================================================================================

## 중복순열 : nπr
## 중복 가능한 n개 중에서 r개를 선택하는 경우의 수 (순서 상관 O)
## nπr = n ** r

# [방법1] : math.factiorial 사용

import sys

n, r = map(int, sys.stdin.readline().split())

n_pi_r = n**r

print(n_pi_r)

# [방법2] : itertools.product, repeat 옵션 사용
# product : 카티젼 곱(cartesian product, 데카르트 곱), 두 개 이상의 리스트의 모든 조합을 구함
# repeat=n : input value(리스트)를 n번 조합하도록 지정 (즉, 조합되는 원소의 수임!)

import sys
from itertools import product

n, r = map(int, sys.stdin.readline().split())

nums = [i for i in range(1, n+1)]
n_pi_r = list(product(nums, repeat=2))

print('경우의 수 : %d개' % len(n_pi_r))
print(n_pi_r)