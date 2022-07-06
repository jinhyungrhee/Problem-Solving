n = int(input())

stack = []

idx = 0
str = ''
for i in range(n): 
  tmp_str = ''
  num = int(input())
  while idx < num:
    idx += 1
    stack.append(idx)
    # print('+')
    tmp_str += '+\n'

  if num == stack[-1]:
    stack.pop()
    # print('-')
    tmp_str += '-\n'
  
  str += tmp_str
  # print(str)
  # print(stack)

if len(stack) == 0:
  print(str[:-1]) # 마지막에 공백(' ')이 들어가있으므로 제외하고 출력
else: # 수열을 만들 수 없는 경우, pop이 제대로 되지 않아 stack에 수가 남게 됨!
  print('NO')