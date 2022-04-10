import sys
n = int(input())
data = list(map(int, input().split()))

add, sub, mul, div = map(int, input().split())

max_val = -sys.maxsize
min_val = sys.maxsize

def dfs(i, now):
  global max_val, min_val, add, sub, mul, div
  if i == n:
    max_val = max(max_val, now)
    min_val = min(min_val, now)
  else:
    if add > 0:
      add -= 1
      dfs(i+1, now + data[i])
      add += 1
    if sub > 0:
      sub -= 1
      dfs(i+1, now - data[i])
      sub += 1
    if mul > 0:
      mul -= 1
      dfs(i+1, now * data[i])
      mul += 1
    if div > 0:
      div -= 1
      # dfs(i+1, now//data[i]) -> 틀린 부분
      dfs(i+1, int(now/data[i]))
      div += 1

#dfs(0, 0) -> 틀린 부분
dfs(1, data[0])

print(max_val)
print(min_val)