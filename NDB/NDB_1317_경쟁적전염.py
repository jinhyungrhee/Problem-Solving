# 경쟁적 전염 - bfs 사용?

''' first attempt
from collections import deque

n, k = tuple(map(int, input().split()))

data = [
  list(map(int, input().split()))
  for _ in range(n)
]

s, a, b = tuple(map(int, input().split()))

# 상 하 좌 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

tmp = [0] * (k + 1)

# 바이러스가 존재하는 위치 큐에 삽입 (낮은 숫자부터 먼저 삽입)
for i in range(n):
  for j in range(n):
    if data[i][j] != 0:
      tmp[data[i][j]] = (i, j)

print(tmp)

def bfs(x, y, num):
  queue = deque()
  queue.append((x, y))
  while queue:
    x, y = queue.popleft()
    # 현재 위치(x, y)에서 네 방향 확인
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      # 공간을 벗어난 경우 무시
      if nx < 0 or nx >= n or ny < 0 or ny >= n:
        continue
      # 이미 다른 숫자로 채워져 있는 경우 무시
      if data[nx][ny] != 0:
        continue
      data[nx][ny] = num
'''

# Hint : 큐에 원소를 낮은 바이러스의 번호부터 삽입
# 너비 우선 탐색으로 방문하지 않은 위치를 차례대로 방문

from collections import deque

n, k = map(int, input().split())

graph = [] # 전체 보드 정보 관리
data = [] # 바이러스 정보 관리

# 보드 정보 입력받을 때 바이러스 정보까지 한꺼번에 처리
for i in range(n):
  # 보드 정보 입력 (줄 단위로 입력)
  graph.append(list(map(int, input().split())))
  for j in range(n):
    # (입력 받은 줄을 탐색하며) 해당 위치에 바이러스가 존재하는 경우
    if graph[i][j] != 0:
      # (바이러스 종류, 시간, x좌표, y좌표) 삽입 ***
      data.append((graph[i][j], 0, i, j))

# 오름차순 정렬 후 큐에 옮김(낮은 번호 바이러스 먼저 증식)
data.sort()
q = deque(data)

target_s, target_x, target_y = map(int, input().split())

# 북 동 남 서 
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# BFS 수행
while q:
  # 가장 낮은 번호의 바이러스 먼저 탐색
  virus, s, x, y = q.popleft()
  # s초가 지나거나 큐가 빌 때까지 반복
  if s == target_s:
    break
  # 현재 노드에서 주변 4가지 위치를 확인
  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]
    # 해당 위치로 이동 가능한 경우
    if 0 <= nx and nx < n and 0 <= ny and ny < n:
      # 아직 방문하지 않았으면 바이러스 주입
      if graph[nx][ny] == 0:
        graph[nx][ny] = virus
        q.append((virus, s+1, nx, ny)) # 중요*** -> 0초 때의 바이러스들이 모두 전파(popleft)된 후 1초때 바이러스들이 전파됨

print(graph[target_x - 1][target_y - 1])
