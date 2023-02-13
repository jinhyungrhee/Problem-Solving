import sys
input = sys.stdin.readline
from collections import deque
INF = int(1e9)
n = int(input())

grid = [
  list(map(int, input().split()))
  for _ in range(n)
]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

now_size = 2
now_x, now_y = 0, 0

# 시작 위치 찾기
for i in range(n):
  for j in range(n):
    if grid[i][j] == 9:
      now_x, now_y = i, j

# 현재 위치에서 모든 위치까지의 최단 거리 계산
def BFS(now_x, now_y):
  target = [[0]*n for _ in range(n)]
  q = deque([])
  q.append((now_x, now_y))

  while q:
    x, y = q.popleft()
    for i in range(4):
      nx, ny = x + dx[i], y + dy[i]
      if 0 <= nx and nx < n and 0 <= ny and ny < n:
        # 자기보다 크기가 같거나 작은 물고기들은 이동 가능
        if grid[nx][ny] <= now_size and target[nx][ny] == 0:
          target[nx][ny] = target[x][y] + 1
          q.append((nx, ny))
  return target

# 최단 거리 테이블에서 먹을 물고기 찾기
def find(dist):
  x, y = 0, 0
  min_val = INF
  for i in range(n):
    for j in range(n):
      # dist[i][j] == 0 : 못가는 곳 / 0 < grid[i][j] < now_size : 먹을 수 있는 물고기 위치
      if dist[i][j] != 0 and grid[i][j] != 0 and grid[i][j] < now_size:
        if min_val > dist[i][j]:
          x, y = i, j
          min_val = dist[i][j]

  if min_val == INF: # 더이상 찾을 물고기가 없는 경우 **
    return None
  else:
    return x, y, min_val

result = 0
ate = 0
while True:
  data = find(BFS(now_x, now_y))
  if data == None:
    print(result)
    break
  else:
    x, y, min_val = data[0], data[1], data[2]
    grid[now_x][now_y] = 0
    grid[x][y] = 9
    result += min_val
    ate += 1
    now_x, now_y = x, y

    if ate == now_size:
      now_size += 1
      ate = 0

# 시간초과