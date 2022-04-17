n, m = map(int, input().split())

# 벽을 세우고 허무는 용도
real_map = [
  list(map(int, input().split()))
  for _ in range(n)
]

# 세운 벽을 copy하여 바이러스 증식시키는 용도
test_map = [[0] * m for _ in range(n)]

max_val = 0
cnt = 0

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def get_score():
  score = 0
  for i in range(n):
    for j in range(m):
      if test_map[i][j] == 0:
        score += 1
  return score

def virus(x, y):
  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]
    if nx < 0 or nx > n - 1 or ny < 0 or ny > m - 1:
      continue
    if test_map[nx][ny] == 0:
      test_map[nx][ny] = 2
      virus(nx, ny)

# Backtracking 이용한 DFS
# def dfs(cnt, x, y):
def dfs(cnt):
    global max_val

    if cnt == 3:
        for i in range(n):
            for j in range(m):
                test_map[i][j] = real_map[i][j]

        for i in range(n):
            for j in range(m):
                if test_map[i][j] == 2:
                    virus(i, j)

        max_val = max(max_val, get_score())
        return 

#   for i in range(4):
#     nx = x + dx[i]
#     ny = y + dy[i]
#     if nx < 0 or nx > n - 1 or ny < 0 or ny > m - 1:
#       continue
#     if real_map[nx][ny] == 0:
#       real_map[nx][ny] = 1
#       cnt += 1
#       dfs(cnt, nx, ny)
#       real_map[nx][ny] = 0
#       cnt -= 1
    '''
    이 부분만 명확히 이해하고 숙지! (dx-dy 테크닉 사용 X)
    '''
    for i in range(n):
        for j in range(m):
            if real_map[i][j] == 0:
                real_map[i][j] = 1
                cnt += 1
                dfs(cnt)
                real_map[i][j] = 0
                cnt -= 1

    return max_val    


print(dfs(0))