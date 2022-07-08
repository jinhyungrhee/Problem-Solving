from collections import deque
import sys

# recursion 최대한도 늘려주기
sys.setrecursionlimit(10**6)

n = int(input())

grid = [
  input()
  for i in range(n)
]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 적록색약X
def DFS(x, y):

  visited[x][y] = True

  for i in range(4):
    nx, ny = x + dx[i], y + dy[i]
    if 0 <= nx and nx < n and 0 <= ny and ny < n:
      if not visited[nx][ny] and grid[x][y] == grid[nx][ny]:
        DFS(nx, ny)

# 적록색약O
def BFS(x, y):
  q = deque([])
  visited[x][y] = True
  q.append((x, y))

  while q:
    curr = q.popleft()
    for i in range(4):
      nx, ny = curr[0] + dx[i], curr[1] + dy[i]
      if 0 <= nx and nx < n and 0 <= ny and ny < n:
        if not visited[nx][ny] and grid[curr[0]][curr[1]] == grid[nx][ny]:
          visited[nx][ny] = True
          q.append((nx, ny))
          

visited = [[False] * n for i in range(n)]
r_g_b_count = 0
for i in range(n):
  for j in range(n):
    if not visited[i][j]:
      DFS(i, j)
      # BFS(i, j)
      r_g_b_count += 1

for i in range(n):
  for j in range(n):
    if grid[i][j] == 'G':
      grid[i] = grid[i].replace(grid[i][j], 'R')

# print(grid)

visited = [[False] * n for i in range(n)]
rg_b_count = 0
for i in range(n):
  for j in range(n):
    if not visited[i][j]:
      BFS(i, j)
      rg_b_count += 1

print(r_g_b_count, rg_b_count)

# DFS 사용시 RecursionError 없애는 방법 :
# sys.setrecursionlimit(10**6) => recursion 최대한도 늘려주기 