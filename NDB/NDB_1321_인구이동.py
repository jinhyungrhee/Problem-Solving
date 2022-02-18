# bfs사용
''' first attempt
from collections import deque

n, l ,r = tuple(map(int, input().split()))

# l <= 인구 차이 <= r

data = [
  list(map(int, input().split()))
  for _ in range(n)
]

temp = [
  [0] * n
  for _ in range(n)
]

# 상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

x, y, cnt = 0, 0, 0

# 각 칸의 인구수 = (연합 인구수) / (연합을 이루는 칸의 개수)
def union(x, y, nx, ny, cnt):
  diff = abs(data[x][y]-data[nx][ny])
  if diff >= l and diff <= r:
    p = (data[x][y] + data[nx][ny]) / cnt
    data[x][y] = p
    data[nx][ny] = p


# BFS 수행
queue = deque()
queue.append((x, y, cnt))

while queue:
  x, y, cnt = queue.popleft()
  # 네 방향 확인
  for i in range(4):
    nx = x + dx[i]
    ny = x + dy[i]
    # 공간 벗어난 경우 무시
    if nx < 0 or nx >= n or ny < 0 or ny >= n:
      continue
    # 다음 노드랑 연합 가능한지 확인
  

print(queue)
'''

from collections import deque

n, l, r = map(int, input().split())

graph = [
  list(map(int, input().split()))
  for _ in range(n)
]

# 상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

result = 0

# 특정 위치에서 출발하여 모든 연합을 체크한 뒤 데이터 갱신
def process(x, y, idx):
  # 현재 위치와 연결된 나라(연합) 정보를 담는 리스트 ***
  united = [] # 매번 초기화 됨
  united.append((x, y))
  # BFS에서 사용할 큐 정의
  q = deque()
  q.append((x, y))
  # 해당 위치 국가에 현재 연합 번호 할당
  union[x][y] = idx
  # 현재 연합의 인구수 임시 저장
  summary = graph[x][y]
  # 현재 연합 국가 수
  count = 1
  # BFS 수행
  while q:
    x, y = q.popleft()
    # 현재 위치에서 네 방향 확인
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if 0 <= nx < n and 0 <= ny < n and union[nx][ny] == -1:
        # 옆 나라와 인구 차이가 L명 이상, R명 이하면 연합 진행
        if l <= abs(graph[nx][ny] - graph[x][y]) <= r:
          # 연합(=동일한 index)에 추가
          q.append((nx, ny))
          union[nx][ny] = idx # 해당 국가에 현재 연합 번호 할당
          summary += graph[nx][ny] # 인구수 추가
          count +=1 # 연합 국가 수 증가
          united.append((nx, ny)) # 기존 국가와 연합된 국가 정보 관리
    
  # 연합 국가끼리 인구 분배(=united 리스트 사용!)***
  for i,j in united:
    graph[i][j] = summary // count
  return count # ?

# 메인 프로그램
total_count = 0

# 더 이상 인구이동 할 수 없을 때까지 반복
while True:
  # union 이차원 배열 생성
  union = [[-1] * n for _ in range(n)]
  idx = 0
  for i in range(n):
    for j in range(n):
      # 해당 나라가 아직 처리되지 않은 경우
      if union[i][j] == -1:
        # 처리 진행
        process(i, j, idx)
        idx += 1

  # 모든 인구이동이 끝난 경우
  if idx == n*n:
    break
  total_count += 1

print(total_count)
