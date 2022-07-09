idx = 0
while True:
  
  l, p, v = map(int, input().split())
  
  if l == 0 and p == 0 and v == 0:
    break

  available = 0

  available += (v // p) * l

  rest = v % p
  if rest <= l: # 남은 날이 이용가능한 날보다 적으면
    available += rest # 남은 날 모두 즐길 수 있음
  else: # 남은 날이 이용가능한 날보다 많으면
    available += l # 이용 가능한 날만 즐김
  idx += 1

  print('Case %d: %d' % (idx, available))