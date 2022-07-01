# 아기 상어 - 220701 (BFS)
from collections import deque
INF = 1e9

n = int(input())
grid = [
  list(map(int, input().split()))
  for _ in range(n)
]

now_size = 2
now_x, now_y = 0, 0

for i in range(n):
  for j in range(n):
    if grid[i][j] == 9: # 시작 위치
      now_x, now_y = i, j
      grid[now_x][now_y] = 0

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 최단 거리 테이블(dist) 구하는 함수(BFS)
def BFS():
  dist = [[-1] * n for _ in range(n)]

  q = deque([(now_x, now_y)])
  dist[now_x][now_y] = 0

  while q:
    x, y = q.popleft()
    for i in range(4):
      nx, ny = x + dx[i], y + dy[i]
      if 0 <= nx and nx < n and 0 <= ny and ny < n:
        # 아기 상어는 자기 자신보다 작거나 같은 물고기만 지나갈 수 있음
        if dist[nx][ny] == -1 and grid[nx][ny] <= now_size:
          dist[nx][ny] = dist[x][y] + 1
          q.append((nx, ny))

  return dist # 매번 갱신된 최단 거리 테이블(dist)을 가지고 find()함수로 새로운 x,y,min_dist값 구할 예정

def find(dist):
  x, y = 0, 0
  min_dist = INF

  for i in range(n):
    for j in range(n):
      # 갈 수 있는 곳이면서 먹을 수 있는 크기의 물고기가 있을 때
      if dist[i][j] != -1 and 0 < grid[i][j] and grid[i][j] < now_size:
        # 가장 가까운 거리의 물고기 찾음
        if min_dist > dist[i][j]:
          min_dist = dist[i][j]
          x, y = i, j

  # 만약 먹을 수 있는 물고기가 하나도 없을 때(min_dist값이 초기값일 때)
  if min_dist == INF:
    return None
  else:
    return x, y, min_dist

# SIMULATION
result = 0 # 이동한 거리(=시간 초)
ate = 0 # 먹은 물고기 수

while True:
  value = find(BFS()) # 처음 시작위치에서 BFS() 수행하고 그 때 먹을 수 있는 물고기 위치, 거리 찾음
  # 더 이상 먹을 수 있는 물고기가 없으면(**종료 조건**)
  if value == None:
    print(result) # 현재까지 이동한 거리 출력
    break # 반복문 종료
  # 아직 먹을 수 있는 물고기가 있으면 (-> 이동)
  else:
    # 현재 위치, 총 이동 거리(=이동 시간), 먹은 물고기 수 갱신
    now_x, now_y = value[0], value[1]
    result += value[2]
    # ** 현재 먹은 위치의 물고기 삭제 ** => 생략하면 답이 나오지 않음!
    grid[now_x][now_y] = 0
    ate += 1

    # 클 수 있는지 확인
    if ate >= now_size:
      now_size += 1
      ate = 0

# 결과 출력 = > 어차피 반드시 if value == None을 거치므로 마지막 결과 출력은 따로 하지 않아도 됨!
# print(result)

''' 1차
from collections import deque

n = int(input())

grid = [
  list(map(int, input().split()))
  for _ in range(n)
]

visited = [[False] * n for _ in range(n)]
dist = [[0] * n for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

size = 2
curr_size = size

# 출발 지점 구하기
now_x, now_y = 0, 0
for i in range(n):
    for j in range(n):
      if grid[i][j] == 9:
        now_x, now_y = i, j

print(now_x, now_y)

def BFS(x, y):
  q = deque()
  q.append([x, y])
  visited[x][y] = True

  while q:
    curr = q.popleft()
    for i in range(4):
      nx, ny = dx[i] + curr[0], dy[i] + curr[1]
      if nx < 0 or nx >= n or ny < 0 or ny >= n:
        continue
      if not visited[nx][ny]:
        visited[nx][ny] = True
        dist[nx][ny] += dist[curr[0]][curr[1]] + 1
        q.append([nx, ny])

# 옮겨진 자리에서 매번 BFS를 수행해야 하나?
BFS(now_x, now_y)

# print(dist)

sec = 0
# while True:
  
target = []
for i in range(n):
  for j in range(n):
    if grid[i][j] > 0 and grid[i][j] < size:
      target.append([i, j, dist[i][j]])
      
# 거리 순으로 정렬 수행
target.sort(key=lambda x:x[2], reverse=True)

print(target)

# target 리스트가 빌때까지 pop해서 거리계산하고 이동함
while target:
  min_x, min_y = target.pop()
  sec += dist[min_x][min_y]
  curr_size -= grid[min_x][min_y]
  grid[min_x][min_y] = 0
  now_x, now_y = min_x, min_y

# min_dist = 987654321
# if len(target) >= 2: # 먹이가 두 개 이상이면 더 가까운 곳 선택
#   for tx, ty in target:
#     if min_dist > dist[tx][ty]:
#       min_dist = dist[tx][ty]
#       min_x = tx
#       min_y = ty

# print(min_x, min_y)

# 둘 중 더 가까운 곳에 먹이를 먹으러 이동
sec += dist[min_x][min_y]
curr_size -= grid[min_x][min_y]
grid[min_x][min_y] = 0 # 먹은 곳의 물고기 삭제
now_x, now_y = min_x, min_y

# 새로운 곳에서 다시 BFS 수행
visited = [[False] * n for _ in range(n)]
dist = [[0] * n for _ in range(n)]
BFS(now_x, now_y)

print(dist)
print(sec)
print(curr_size)
'''