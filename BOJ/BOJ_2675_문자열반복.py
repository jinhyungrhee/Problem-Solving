tc = int(input())

for _ in range(tc):
  result = ''
  r, str = input().split()
  for s in str:
    result += s * int(r)

  print(result)