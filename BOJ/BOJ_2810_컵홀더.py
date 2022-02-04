n = int(input())

S = input()

cnt = 0
for i in S:
  if i == 'L':
    cnt += 1

if cnt == 0:
  print(n)
else:
  print(n - ((cnt // 2) - 1))