from collections import deque
INF = 1e9

n = int(input())

array = [
  list(map(int, input().split()))
  for _ in range(n)
]

# 아기상어의 크기와 위치
now_size = 2
now_x, now_y = 0, 0

# 아기상어 위치 찾기
for i in range(n):
  for j in range(n):
    if array[i][j] == 9:
      now_x, now_y = i, j
      # 찾은 자리 빈칸으로 변경
      array[i][j] = 0

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 모든 거리까지의 최단 거리 계산하는 BFS 함수
def bfs():
  # dist 배열을 -1로 초기화 (-1: '도달할 수 없음' 의미)
  # dist 배열은 도달할 수 있는지 없는지 + 최단 거리만 판단!
  dist = [[-1] * n for i in range(n)]
  q = deque([(now_x, now_y)])
  dist[now_x][now_y] = 0 # 시작 위치는 도달이 가능함(거리: 0)

  while q:
    x, y = q.popleft()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if 0 <= nx < n and 0 <= ny < n:
        # 자신의 크기보다 작거나 같은 경우에만 지나갈 수 있음
        if dist[nx][ny] == -1 and array[nx][ny] <= now_size:
          dist[nx][ny] = dist[x][y] + 1
          q.append((nx, ny))
  # 모든 위치까지의 최단 거리 테이블 반환
  return dist           

# 최단 거리 테이블이 주어졌을 때, 먹을 물고기를 찾는 함수
def find(dist):
  x, y = 0, 0
  min_dist = INF
  for i in range(n):
    for j in range(n):
      # '도달이 가능'하면서 '먹을 수 있는 물고기'일 때
      if dist[i][j] != -1 and 1 <= array[i][j] and array[i][j] < now_size:
        # 가장 가까운 물고기 한마리 선택 (최소값 찾기)
        if dist[i][j] < min_dist:
          x, y = i, j
          min_dist = dist[i][j] 
  if min_dist == INF: # 먹을 수 있는 물고기가 없는 경우
    return None
  else:
    return x, y, min_dist # 먹을 물고기 위치와 거리

result = 0 # 최종 답안
ate = 0 # 현재 크기에서 먹은 양

while True:
  # 먹을 수 있는 물고기 위치 찾기
  value = find(bfs())
  # 먹을 수 있는 물고기가 없으면, 현재까지 움직인 거리 출력
  if value == None:
    print(result)
    break
  else:
    # 이동하여 물고기 먹기
    now_x, now_y = value[0], value[1]
    result += value[2]
    # 먹은 위치 비우기
    array[now_x][now_y] = 0
    ate += 1
    # 자신의 현재 크기 이상으로 먹은 경우, 크기 증가
    if ate >= now_size:
      now_size += 1
      ate = 0 # ate 초기화