import sys
input = sys.stdin.readline

n = int(input())
p = n * n

# 전체 강의실(grid)
classroom = [[0] * n for _ in range(n)]
# 좋아하는 학생들과 앉았는지 확인하기 위한 리스트(이차원리스트)
like_room = [[] for _ in range(p + 1)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for _ in range(p):
  data = list(map(int, input().split()))
  like = data[1:]
  like_room[data[0]] = like # 학생별 좋아하는 학생 정보 저장
  # if p == 0: # 첫 번째 학생에 대해서 굳이 따로 처리해주지 않아도 됨 ->> 조건에 의해서 저절로 처리되기 때문
  #   classroom[1][1] = data[0]
  #   continue
  temp = []
  for i in range(n):
    for j in range(n):
      sum_like, sum_empty = 0, 0
      if classroom[i][j] != 0: # 빈자리가 아니면 skip
        continue
      for k in range(4): # 주변 탐색
        nx = i + dx[k]
        ny = j + dy[k]
        if nx < 0 or nx > n - 1 or ny < 0 or ny > n - 1: # 범위 벗어난 경우 skip
          continue
        if classroom[nx][ny] in like:
          sum_like +=1 
        if classroom[nx][ny] == 0:
          sum_empty += 1
      # 주변 탐색이 끝나면, temp리스트에 누적된 값들 저장
      temp.append((sum_like, sum_empty, (i, j)))
  # 저장된 값들을 sum_like, sum_empty 순서로 내림차순, 좌표 열 기준으로 오름차순으로 정렬
  temp.sort(key=lambda x:(-x[0], -x[1], x[2]))

  # temp 리스트에서 가장 최상위(0번째)로 올라온 튜플의 좌표를 사용해 자리배정
  classroom[temp[0][2][0]][temp[0][2][1]] = data[0]

# 만족도 조사
sum_answer = 0
for i in range(n):
  for j in range(n):
    answer = 0
    for k in range(4): # 주변에 선호하는 친구가 있는지 확인
      nx = i + dx[k]
      ny = j + dy[k]
      if nx < 0 or nx > n - 1 or ny < 0 or ny > n - 1: # 범위 벗어나면 skip
        continue
      if classroom[nx][ny] in like_room[classroom[i][j]]:
        answer += 1
        continue
    # 주변 탐색이 끝나면 점수 합산
    if answer != 0:
      sum_answer += (10 ** (answer - 1))

print(sum_answer)

