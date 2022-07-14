s = input()
check = input()
n = len(check)

stack = []

for i in range(len(s)):

  stack.append(s[i])
  
  if stack and ''.join(stack[-n:]) == check:
    for i in range(n):
      stack.pop()

if len(stack) == 0:
  print("FRULA")
else:
  print(''.join(stack))
    