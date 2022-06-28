# 220628

n = int(input())

data = list(map(int, input().split()))

data.sort()

print(data)

num_of_member = 0
num_of_group = 0
for i in range(len(data)):
  num_of_member += 1
  if data[i] <= num_of_member:
    num_of_group += 1
    num_of_member = 0

print(num_of_group)

#1 
# '현재 그룹에 포함된 모험가의 수'가 '현재 확인하고 있는 공포도'보다 크거나 같다면, 이를 그룹으로 설정
# 공포도 오름차순 정렬 - 항상 최소한의 모험가의 수만 포함하여 그룹을 결성. 최대한 많은 그룹이 구성됨 (= 최적의 해)
# => 보완 필요!
'''
n = int(input())
data = list(map(int, input().split()))

data.sort() # O(nlogn)

count = 0

while n-1 >= 0: # n-1은 인덱스

  fear = data[n-1]
  
  while fear != 0:
    fear -= 1
    n -= 1
  
  count += 1

print(count)
'''