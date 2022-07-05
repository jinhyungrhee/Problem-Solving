data = list(input())

str = []
rev = []
mid = []

while data:
  curr = data.pop(0)
  if curr in data:
    rev.append(data.pop(data.index(curr)))
    str.insert(0, curr)
  else:
    mid.append(curr)


str.sort()
rev.sort(reverse=True)
result = str + mid + rev

# 팰린드롬이 되려면 mid 리스트에 들어가는 알파벳이 1개 or 0개이어야 함
if len(mid) > 1:
  print("I'm Sorry Hansoo")
else:
  print(''.join(result))