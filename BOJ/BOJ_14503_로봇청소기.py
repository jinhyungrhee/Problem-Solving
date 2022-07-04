n, m = map(int, input().split())


x, y, dir_num = map(int, input().split())


# 반시계방향(왼쪽 회전) : 북 서 남 동
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

grid = [
  list(map(int, input().split()))
  for _ in range(n)
]

def in_range(x, y):
  return 0 <= x and x < n and 0 <= y and y < m

def turn_left(dir_num):
  dir_num = (dir_num + 1) % 4
  return dir_num

def turn_around(dir_num):
  dir_num = (dir_num + 2) % 4
  return dir_num

# 1은 3으로, 3은 1로 변경
if dir_num % 2 != 0:
  dir_num  = (dir_num + 2) % 4

# 처음 현재 위치 청소(청소한 곳 2로 변경)
grid[x][y] = 2
turn_count = 0
result = 1

while True:
    # 방향 전환 (왼쪽으로 회전)
    dir_num = turn_left(dir_num)
    turn_count += 1
    # 현재 위치에서 인접한 칸 탐색
    nx, ny = x + dx[dir_num], y + dy[dir_num]
    if in_range(nx, ny) and grid[nx][ny] == 0:
        # 한칸 전진 후 청소
        x, y = x + dx[dir_num], y + dy[dir_num]
        grid[x][y] = 2
        result += 1
        turn_count = 0 # 초기화

    if turn_count == 4:
        # 주의 : 뒤로 한칸 후진할 때 바라보는 방향이 바뀌면 안 됨! ** 
        back_dir = turn_around(dir_num)
        bx, by = x + dx[back_dir], y + dy[back_dir]
        if in_range(bx, by) and grid[bx][by] == 1:
            break
        else:
            # 뒤로 한칸 후진
            x, y = x + dx[back_dir], y + dy[back_dir]
        turn_count = 0


print(result)