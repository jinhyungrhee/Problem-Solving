n, m = map(int, input().split())

# 원본 맵(backtracking으로 벽을 세웠다가 없앴다가를 반복)
data = [
  list(map(int, input().split()))
  for _ in range(n)
]

# 초기 맵에 3개의 벽을 설치한 뒤에 결과를 복사할 임시 맵(바이러스 전파를 실험할 맵)
tmp = [[0]*m for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

result = 0

# dfs를 이용한 virus 함수
def virus(x, y):
  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]
    # if nx < 0 or nx > n - 1 or ny < 0 or ny > m - 1:
    #   continue
    if nx >= 0 and nx < n and ny >= 0 and ny < m:
      # 벽을 설치한 뒤의 맵에서 빈칸이 있으면 바이러스 살포
      if tmp[nx][ny] == 0: 
        tmp[nx][ny] = 2
        virus(nx, ny)

# 바이러스 살포된 뒤 안전 영역 크기 계산하는 함수
def get_score():
  score = 0
  for i in range(n):
    for j in range(m):
      if tmp[i][j] == 0:
        score += 1
  return score

# DFS(Backtracking을 이용한 완전탐색)로 매번 울타리 설치하고 안전 영역 검사
def dfs(count):
  global result
  # 종료조건
  if count == 3:
    for i in range(n):
      for j in range(m):
        # 벽을 3개 세웠으므로 임시맵에 복사
        tmp[i][j] = data[i][j]
    for i in range(n):
      for j in range(m):
        # 바이러스 실험과 점수 계산은 임시맵에 대해서 실행
        if tmp[i][j] == 2:
          virus(i, j)
    # 바이러스 실험과 점수 계산은 임시맵에 대해서 실행
    result = max(result, get_score())
    return 

  # 원본 맵에서 Backtracking으로 울타리 설치-제거 반복
  for i in range(n):
    for j in range(m):
      if data[i][j] == 0:
        data[i][j] = 1
        count += 1
        dfs(count)
        # return 되어 나오면 울타리 제거
        data[i][j] = 0
        count -= 1

dfs(0)
print(result)