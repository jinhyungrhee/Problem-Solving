str = input()

cnt = 1
for i in range(1, len(str)):
  if ord(str[i-1]) >= ord(str[i]):
    cnt += 1

print(cnt)