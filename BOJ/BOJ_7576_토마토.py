from collections import deque
m, n = map(int, input().split())

box = [
  list(map(int, input().split()))
  for _ in range(n)
]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

dist = [[0]*m for _ in range(n)]
visited = [[False]*m for _ in range(n)]

q = deque([])
minus_count = 0
for i in range(n):
  for j in range(m):
    if box[i][j] == -1:
      minus_count += 1
    if box[i][j] == 1:
      q.append((i, j))
      visited[i][j] = True

while q:
  x, y = q.popleft()
  for i in range(4):
    nx, ny = x + dx[i], y + dy[i]
    if 0 <= nx and nx < n and 0 <= ny and ny < m:
      if visited[nx][ny] == False and box[nx][ny] != -1:
        dist[nx][ny] = dist[x][y] + 1
        visited[nx][ny] = True
        q.append((nx, ny))

# print(dist)
# print(visited)

max_val = 0
nv_count = 0
for i in range(n):
  for j in range(m):
    if visited[i][j] == False:
      nv_count += 1
    if max_val < dist[i][j]:
      max_val = dist[i][j]

# print(minus_count)
# print(nv_count)

if nv_count > minus_count:
  print(-1)
else:
  print(max_val)