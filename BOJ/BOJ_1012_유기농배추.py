# BFS 사용
from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

tc = int(input())

def BFS(x, y):

  q = deque([])
  q.append((x, y))
  visited[x][y] = True
  
  while q:
    curr = q.popleft()
    
    for i in range(4):
      nx, ny = curr[0] + dx[i], curr[1] + dy[i]
      if 0 <= nx and nx < r and 0 <= ny and ny < c:
        if not visited[nx][ny] and grid[nx][ny] == 1:
          visited[nx][ny] = True
          q.append((nx, ny))

for _ in range(tc):
  r, c, n = map(int, input().split())
  grid = [[0] * c for _ in range(r)]
  visited = [[False] * c for _ in range(r)]
  # graph 입력 받기
  for _ in range(n):
    x, y = map(int, input().split())
    grid[x][y] = 1

  count = 0
  # DFS 수행
  for i in range(r):
    for j in range(c):
      if not visited[i][j] and grid[i][j] == 1:
        BFS(i, j)
        count += 1

  print(count)


# DFS RecursionError 발생 -> 해결가능한지?
'''
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

tc = int(input())

def DFS(x, y):

  visited[x][y] = True

  for i in range(4):
    nx, ny = x + dx[i], y + dy[i]
    if 0 <= nx and nx < r and 0 <= ny and ny < c:
      if not visited[nx][ny] and grid[nx][ny] == 1:
        visited[nx][ny] = True
        DFS(nx, ny)

for _ in range(tc):
  r, c, n = map(int, input().split())
  grid = [[0] * c for _ in range(r)]
  visited = [[False] * c for _ in range(r)]
  # graph 입력 받기
  for _ in range(n):
    x, y = map(int, input().split())
    grid[x][y] = 1

  count = 0
  # DFS 수행
  for i in range(r):
    for j in range(c):
      if not visited[i][j] and grid[i][j] == 1:
        DFS(i, j)
        count += 1

  print(count)
'''
# => 적절한 종료조건을 설정해주면 RecursionError를 처리할 수 있나?