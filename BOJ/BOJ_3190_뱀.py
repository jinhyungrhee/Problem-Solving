# 사과 = 1, 뱀 = 2
n = int(input())
k = int(input())

grid = [[0] * (n+1) for _ in range(n+1)]
# 방향 회전 정보 저장
info = []

for _ in range(k):
  x, y = map(int, input().split())
  grid[x][y] = 1 # 사과 위치 : 1

# 방향 회전 정보
l = int(input())
for _ in range(l):
  x, c = list(map(str, input().split()))
  info.append((int(x), c))

# 시계방향(동남서북)
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

# 방향 전환 함수
def turn(dir_num, c):
  if c == 'L':
    dir_num = (dir_num - 1) % 4
  else: # c == 'R'
    dir_num = (dir_num + 1) % 4
  return dir_num

def simulate():
  x, y = 1, 1 # 시작위치
  grid[x][y] = 2 # 뱀 위치 : 2
  dir_num = 0 # 시작 방향 : '동쪽'
  t = 0 # 초 정보
  idx = 0 # 회전 횟수(순서) *
  q = [(x, y)] # 뱀 전체 위치 저장(꼬리가 앞) *
  while True:
    nx = x + dx[dir_num]
    ny = y + dy[dir_num]
    if 1 <= nx and nx <= n and 1 <= ny and ny <= n and grid[nx][ny] != 2:
      # 사과 없는 경우
      if grid[nx][ny] == 0:
        # 머리 이동
        grid[nx][ny] = 2
        q.append((nx, ny))
        # 꼬리 제거
        px, py = q.pop(0)
        grid[px][py] = 0
      # 사과 있는 경우
      if grid[nx][ny] == 1:
        # 머리만 이동
        grid[nx][ny] = 2
        q.append((nx, ny))
    else: # 안전하지 않은 위치인 경우
      t += 1
      break # 종료
    # 공통
    x, y = nx, ny
    t += 1
    # 회전해야 하는 경우(흐른 시간과 일치하는지 확인)
    if idx < l and t == info[idx][0]:
      dir_num = turn(dir_num, info[idx][1])
      idx += 1
  return t

print(simulate())