tc = int(input())

for _ in range(tc):
  h, w, n = map(int, input().split())

  floor = n % h
  if floor == 0:
    floor = h
    room_num = n//h
  else:
    room_num = n//h + 1

  floor = str(floor)  
  if room_num < 10:
    room_num = '0' + str(room_num)
  else:
    room_num = str(room_num)

  print(floor + room_num)