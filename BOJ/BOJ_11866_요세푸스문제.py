from collections import deque

n, m = map(int, input().split())

q = deque([])

for i in range(1, n + 1):
  q.append(i)

times = m - 1
result = []
while q:

  while times > 0:
    curr = q.popleft()
    q.append(curr)
    times -= 1

  curr = q.popleft()
  result.append(curr)
  times = m - 1

print("<", end="")
for i in range(len(result)-1):
  print(result[i], end=", ")

print(result[-1], end=">")