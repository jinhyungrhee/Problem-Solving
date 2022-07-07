# 실버5
import math

n = int(input())

data = list(map(int, input().split()))

m = max(data)

# 숫자 배열 생성
nums = [0] * (m + 1)
for i in range(2, m + 1):
  nums[i] = i

# 에라토스테네스의 체
for i in range(2, int(math.sqrt(m)) + 1):
  if nums[i] == 0:
    continue
  for j in range(i + i, m + 1, i):
    nums[j] = 0

nums = set(nums)
data = set(data)

print(len(nums & data))