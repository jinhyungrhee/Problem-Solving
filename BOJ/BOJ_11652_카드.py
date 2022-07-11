import sys
n = int(sys.stdin.readline())

num_dict = {}
for _ in range(n):
  num = int(sys.stdin.readline().rstrip())
  if num not in num_dict:
    num_dict[num] = 1
  else:
    num_dict[num] = num_dict.get(num) + 1

# print(num_dict)
nums = sorted(num_dict.items(), key=lambda x:(-x[1], x[0]))
print(nums[0][0])  


# collections.defaultdict 사용
'''
import sys
from collections import defaultdict
n = int(sys.stdin.readline())

num_dict = defaultdict(int)
for _ in range(n):
  num = int(sys.stdin.readline().rstrip())
  num_dict[num] += 1

# print(num_dict)
nums = sorted(num_dict.items(), key=lambda x:(-x[1], x[0]))
print(nums[0][0])  
'''