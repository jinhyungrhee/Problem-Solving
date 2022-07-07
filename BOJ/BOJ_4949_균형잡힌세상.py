PS = ['[', ']', '(', ')']

while True:
  str = input()
  
  if str == '.':
    break

  n = len(str)
  stack = []
  for i in range(n):
    if str[i] in PS:
      if str[i] == '(' or str[i] == '[':
        stack.append(str[i])
      else: # ')' 이거나 ']'이면
        if stack and str[i] == ')' and stack[-1] == '(':
          stack.pop()
        elif stack and str[i] == ']' and stack[-1] == '[':
          stack.pop()
        else:
          stack.append(str[i])

  if len(stack) == 0:
    print("yes")
  else:
    print("no")