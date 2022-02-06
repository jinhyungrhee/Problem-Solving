'''
구현 - Brute Forcing
'''

# 생성자로 만들어지는 숫자 먼저 구하여 리스트 저장
result = []
for i in range(1, 10001):
  result.append(sum(map(int, str(i))))
  result[i-1] += i

#print(sorted(result))

# for 1 ~ 10000까지 탐색하며 리스트에 없는 숫자 출력
for i in range(1, 10001):
  if i not in result:
    print(i)

