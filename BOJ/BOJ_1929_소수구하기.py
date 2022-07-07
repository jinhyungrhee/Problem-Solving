# 실버3
import math

n, m = map(int, input().split())

# 숫자 배열 생성
nums = [0] * (m + 1)

for i in range(2, m + 1):
  nums[i] = i

# 에라토스테네스의 체
for i in range(2, int(math.sqrt(m))+1):
  if nums[i] == 0:
    continue
  for j in range(i + i, m + 1, i):
    nums[j] = 0

nums = list(set(nums))
nums.sort()
print(nums)

for num in nums:
  if num >= n:
    print(num)