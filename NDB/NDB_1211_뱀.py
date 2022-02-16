'''first try
n = int(input())
k = int(input())

grid = [
  [0] * n
  for _ in range(n)
]

# 사과 깔기
for _ in range(k):
  x, y = tuple(map(int, input().split()))
  grid[x-1][y-1] = 1
  
# 시작 위치 (0, 0)
x, y = 0, 0
# 맨 처음에는 방향이 '오른쪽'을 향함
dir_num = 0 # 동 남 서 북
dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]

def in_range(x, y):
  return 0 <= x and x < n and 0 <= y and y < n

cnt = 0
flag = True
l = int(input())
for _ in range(l): # 횟수
  t, c_dir = input().split()
  t = int(t)
  for i in range(1, t+1): # 초
    nx, ny = x + dx[dir_num], y + dy[dir_num]
    # 다음 이동할 칸이 자기 몸이나 벽이면 종료
    if grid[nx][ny] == -1 or in_range(nx, ny) == False:
      #cnt += i
      flag = False
      break
    # 사과가 있으면
    if grid[nx][ny] == 1:
      # 이전 위치 몸통(-1)으로 표시
      grid[x][y] = -1
      # 머리 위치 변경
      x, y = nx, ny
    else:
    # 사과가 없으면 머리 위치 변경하고 꼬리 있던 지점 원위치(0)
      grid[x][y] = 0
      x, y = nx, ny
    cnt += i
  # 시간 초 지나면 방향 전환
  if c_dir == 'L':
    dir_num = (dir_num + 3) % 4
  elif c_dir == 'D':
    dir_num = (dir_num + 1) % 4
  # 몸이나 벽에 닿았는지 확인
  if flag == False:
    break

print(cnt)
'''

n = int(input())
k = int(input())
data = [[0] * (n + 1) for _ in range(n + 1)] # 맵 정보(0은 사용X)
info = [] # 방향 회전 정보

# 맵 정보 : 사과 위치 1로 표시
for _ in range(k):
  a, b = map(int, input().split())
  data[a][b] = 1

# 방향 회전 정보 입력
l = int(input())
for _ in range(l):
  x, c = input().split()
  info.append((int(x), c)) # 튜플 형태로 저장

# 동 남 서 북 (시계방향)
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def turn(direction, c):
  if c == "L":
    direction = (direction - 1) % 4 # 음수가 나오는 경우?
  else:
    direction = (direction + 1) % 4
  return direction

def simulate():
  # 시작 위치
  x, y = 1, 1
  data[x][y] = 2 # 뱀이 존재하는 위치 : 2
  direction = 0 # 시작 방향 : 동(dx[0]+dy[0])
  t = 0 # 지난 초
  idx = 0 # 다음에 회전할 정보 ***
  q = [(x, y)] # 뱀이 차지하는 위치 정보(꼬리가 앞쪽)
  while True:
    nx = x + dx[direction]
    ny = y + dy[direction]
    # 다음 위치가 맵 안에 있고 뱀의 몸통이 없는 위치라면(= 안전한 위치)
    if 1 <= nx and nx <= n and 1 <= ny and ny <= n and data[nx][ny] != 2:
      # 사과가 없는 경우
      if data[nx][ny] == 0:
        # 머리 이동 - 맵 정보에 기록
        data[nx][ny] = 2
        # 머리 이동 - 뱀 정보에 기록
        q.append((nx, ny))
        # 이동 후 꼬리 제거 - 뱀 정보에 기록
        px, py = q.pop(0)
        # 이동 후 꼬리 제거 - 맵 정보에 기록
        data[px][py] = 0
      # 사과가 있는 경우
      if data[nx][ny] == 1:
        # 머리 이동만 기록한 후 꼬리 그대로 둠
        data[nx][ny] = 2
        q.append((nx, ny))
    # 다음 위치가 벽이나 몸통이라면 (= 안전하지 않은 위치)
    else:
      t += 1
      break # 종료
    # 공통 처리 부분
    x, y = nx, ny # x,y값 갱신
    t += 1
    # 회전할 시간인 경우 회전 ***
    if idx < l and t == info[idx][0]:
      direction = turn(direction, info[idx][1])
      idx += 1
  return t

print(simulate())