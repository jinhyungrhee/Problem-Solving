import sys
from collections import Counter

n = int(sys.stdin.readline())

data = []

for _ in range(n):
  data.append(int(sys.stdin.readline()))

data.sort()
sum_val = sum(data)
c_data = Counter(data).most_common(2)

# 출력 
print(round(sum_val/n))
print(data[n//2])
if len(c_data) == 2 and c_data[0][1] == c_data[1][1]:
  print(c_data[1][0])
else:
  print(c_data[0][0])
print(data[-1] - data[0])