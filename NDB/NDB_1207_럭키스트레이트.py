'''
#1 sum변수를 1개만 가지고도 구현 가능!
'''

number = input()
n = len(number)

sum1 = 0
for i in range(n//2):
  sum1 += int(number[i])

sum2 = 0
for j in range(n//2, n):
  sum2 += int(number[j])

if sum1 == sum2:
  print("LUCKY")
else:
  print("READY")
