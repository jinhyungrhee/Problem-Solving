# 완전탐색 DFS 사용
import sys
n = int(input())

number = list(map(int, input().split()))

add, sub, mul, div = map(int, input().split())

min_val = sys.maxsize
max_val = -sys.maxsize

def dfs(i, now):
  global min_val, max_val, add, sub, mul, div
  # 모든 연산자 사용한 경우, 최솟값과 최댓값 업데이트
  if i == n:
    min_val = min(min_val, now)
    max_val = max(max_val, now)
  else:
    # 각 연산자에 대해 재귀적으로 수행
    if add > 0:
      add -= 1
      dfs(i + 1, now + number[i])
      add += 1 # 리턴되어 나왔을 때 다시 복구
    if sub > 0:
      sub -= 1
      dfs(i + 1, now - number[i])
      sub += 1
    if mul > 0:
      mul -= 1
      dfs(i + 1, now * number[i])
      mul += 1
    if div > 0:
      div -= 1
      dfs(i  + 1, int(now / number[i])) # 나눌 때는 나머지 제거
      div += 1

# dfs 호출
dfs(1, number[0])

# 출력
print(max_val)
print(min_val)



'''중복순열 사용
from itertools import product

n = 4
print(list(product(['+', '-', '*', '/'], repeat=(n-1))))
'''