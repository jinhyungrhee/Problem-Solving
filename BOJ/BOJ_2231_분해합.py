n = int(input())
INF = 1e9

min_val = INF
for i in range(1, n+1):
  data = list(str(i))
  tmp = 0
  for d in data:
    tmp += int(d)
  made_num = i + tmp
  if made_num == n and i < min_val:
    min_val = i
    # print(i, made_num)

if min_val == INF:
  print(0)
else:
  print(min_val)