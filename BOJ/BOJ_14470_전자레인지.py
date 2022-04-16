meat_temp = int(input())
target_temp = int(input())
c = int(input()) # 0도 미만
d = int(input()) # 0도 (해동)
e = int(input()) # 0도 초과

if meat_temp < 0:
  cnt = e
else:
  cnt = 0

while meat_temp < target_temp:
  if meat_temp < 0:
    cnt += c
  elif meat_temp == 0:
    cnt += d
  elif meat_temp > 0:
    cnt += e
  meat_temp += 1

print(cnt)