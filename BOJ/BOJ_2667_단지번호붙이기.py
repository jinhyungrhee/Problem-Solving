n = int(input())

grid = [
  input()
  for _ in range(n)
]

visited = [[False] * n for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def DFS(x, y):

  visited[x][y] = True

  for i in range(4):
    global count
    nx, ny = x + dx[i], y + dy[i]
    if 0 <= nx and nx < n and 0 <= ny and ny < n:
      if not visited[nx][ny] and grid[nx][ny] == '1':
        count += 1
        DFS(nx, ny)
  
complex = []
for i in range(n):
  for j in range(n):
    count = 1
    if not visited[i][j] and grid[i][j] == '1':
      DFS(i, j)
      complex.append(count)

# print(visited)
# print(complex)
print(len(complex))
complex.sort()
for c in complex:
  print(c)