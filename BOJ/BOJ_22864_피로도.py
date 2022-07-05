A, B, C, M = map(int,input().split())

hour = 0
piro = 0
work = 0

while hour < 24:
  next_piro = piro + A

  if next_piro <= M:
    piro += A
    work += B
  else:
    if piro - C < 0:
      piro = 0
    else:
      piro -= C

  hour += 1

print(work)