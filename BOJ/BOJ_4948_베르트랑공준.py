import math

max_num = 2 * 123456

nums = [0] * (max_num + 1)

for i in range(1, max_num + 1):
  nums[i] = i

# 에라토스테네스의 체
for i in range(2, int(math.sqrt(max_num)) + 1):
  for j in range(i + i, max_num + 1, i):
    if nums[j] == 0:
      continue
    nums[j] = 0

while True:
  n = int(input())

  if n == 0:
    break
    
  s = n
  e = 2 * n
    
  # n보다 크고 2n보다 작거나 같음
  count = 0
  for n in nums[s+1:e+1]:
    if n != 0:
      count += 1
  
  print(count)