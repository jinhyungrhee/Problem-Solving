import sys

input = sys.stdin.readline

n = int(input())

array = list(map(int, input().split()))

m = int(input()) # 총 예산

start = 0
end = max(array)
result = 0

while start <= end:

  # mid가 상한액(m)
  mid = (start + end) // 2

  sum_val = 0
  # 상한액(m)보다 크면 잘라냄
  for i in array:
    if i > mid:
      sum_val += mid
    else:
      sum_val += i

  if sum_val <= m: # 상한액이 더 커져야함(=오른쪽 탐색)
      result = mid
      start = mid + 1
  else: # 상한액이 더 작아져야함(=왼쪽 탐색)
      end = mid - 1


print(result)