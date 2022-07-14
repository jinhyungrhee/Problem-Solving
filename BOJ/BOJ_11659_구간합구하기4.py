import sys
n, m = map(int, sys.stdin.readline().split())

data = list(map(int, sys.stdin.readline().split()))

sum_val = 0
for i in range(len(data)):
  sum_val += data[i]
  data[i] = sum_val

# print(data)

for _ in range(m):
  s, e = map(int, sys.stdin.readline().split())
  if s == 1:
    print(data[e-1])
  else:
    print(data[e-1] - data[s-2])