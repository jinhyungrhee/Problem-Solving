n, m = map(int, input().split())

grid = [
  list(map(int, input().split()))
  for _ in range(n)
]

# 벽을 설치한 뒤의 맵
tmp = [[0] * m for _ in range(n)]

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
result = 0

def in_range(x, y):
  return 0 <= x < n and 0 <= y < m

# 바이러스 생성
def virus(x, y):
  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]
    if in_range(nx, ny):
      if tmp[nx][ny] == 0:
        # 해당 위치에 바이러스 생성 후 재귀호출
        tmp[nx][ny] = 2
        virus(nx, ny)

# 안전 영역 계산
def get_score():
  score = 0
  for i in range(n):
    for j in range(m):
      if tmp[i][j] == 0:
        score += 1
  return score

# DFS로 울타리 설치하고 안전 영역 계산
def dfs(count):
  global result
  if count == 3: # 울타리 3개인 경우
    for i in range(n):
      for j in range(m):
        # tmp로 오리지널 맵 복사
        tmp[i][j] = grid[i][j]

    # 각 바이러스 위치에서 전파 진행
    for i in range(n):
      for j in range(m):
        if tmp[i][j] == 2:
          virus(i, j)

    # 안전 영역 최댓값 계산
    result = max(result, get_score())
    return
  
  # 빈공간에 울타리 설치
  for i in range(n):
    for j in range(m):
      if grid[i][j] == 0:
        grid[i][j] += 1
        count += 1
        dfs(count)
        grid[i][j] -= 1
        count -= 1

dfs(0)
print(result)


'''
시간복잡도 체크 필요
'''