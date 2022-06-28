# 220628

data = input()

alpha = []
num = 0
for d in data:
  if d.isalpha():
    alpha.append(d)
  else:
    num += int(d)

alpha.sort()

answer = ''.join(alpha) + str(num)

print(answer)

#1 배열 하나와 isalpha() 사용하여 해결 가능!
'''
string = input()

ascii = []
number = []
for i in string:
  if ord(i) >= 65 and ord(i) <= 90:
    ascii.append(i)
  else:
    number.append(int(i))

sorted(ascii)
res_str = ''.join(sorted(ascii))
res_num = sum(number)
print(res_str + str(res_num))
'''