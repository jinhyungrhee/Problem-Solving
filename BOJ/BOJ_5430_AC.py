from collections import deque
tc = int(input())

for _ in range(tc):
  reverse = 0 # 0이면 popleft() 1이면 pop()
  is_error = False
  order = input()
  n = int(input())
  data = input()
  if data == '[]':
    q = deque()
  else:
    data = list(map(int, data[1:-1].split(',')))
    q = deque(data)

  for o in order:
    if o == 'R':
      reverse = (reverse + 1) % 2
    elif o == 'D':
      if len(q) == 0:
        is_error = True
        break
      if reverse == 0:
        q.popleft()
      elif reverse == 1:
        q.pop()

  listed_q = list(q)
  
  if is_error:
    print('error')
  else:
    if len(listed_q) == 0:
      print([])
    else:
      if reverse == 0: # 앞에서부터 출력
        print('[', end='')
        for i in range(len(listed_q)-1):
          print(listed_q[i], end=',')
        print(listed_q[-1], end=']')
        print()
          
      else: # 뒤에서부터 출력
        print('[', end='')
        for i in range(len(listed_q)-1, 0, -1):
          print(listed_q[i], end=',')
        print(listed_q[0], end=']')
        print()