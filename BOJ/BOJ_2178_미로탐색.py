from collections import deque

n, m = map(int, input().split())

grid = [
  input()
  for _ in range(n)
]

dist = [[0]*m for i in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

s, e = 0, 0

q = deque([])
q.append((s, e))
dist[s][e] = 1

while q:

  x, y = q.popleft()

  for i in range(4):
    nx, ny = x + dx[i], y + dy[i]
    if 0 <= nx and nx < n and 0 <= ny and ny < m:
      if dist[nx][ny] == 0 and grid[nx][ny] != '0':
        q.append((nx, ny))
        dist[nx][ny] = dist[x][y] + 1

print(dist[n-1][m-1])