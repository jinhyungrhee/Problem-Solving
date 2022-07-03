n = int(input())
target = int(input())

grid = [[0] * (n + 1) for _ in range(n + 1)]

# 아래, 오른쪽, 위, 왼쪽
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def in_range(x, y):
  return 0 < x and x <= n and 0 < y and y <= n

# 시작 조건 초기화
x, y = 1, 1
dir_num = 0
grid[x][y] = n * n

# 뒤에서부터 입력
for i in range(n*n - 1, 0, -1):

  # 다음 이동해야 할 곳 체크
  nx, ny = x + dx[dir_num], y + dy[dir_num]

  # 이동할 수 없다면 방향 전환!
  if not in_range(nx, ny) or grid[nx][ny] != 0:
    dir_num = (dir_num + 1) % 4

  # x,y 값 갱신
  x, y = x + dx[dir_num], y + dy[dir_num]
  grid[x][y] = i


# 출력
for i in range(1, n+1):
  for j in range(1, n+1):
    print(grid[i][j], end=' ')
  print()

for i in range(1, n+1):
  for j in range(1, n+1):
    if grid[i][j] == target:
      print(i, j)