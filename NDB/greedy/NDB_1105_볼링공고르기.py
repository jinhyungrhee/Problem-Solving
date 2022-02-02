''' 
#1 시간복잡도 : O(n^2) -> 조금 더 개선 가능!
'''

n, m = map(int, input().split())

data = list(map(int, input().split()))

count = 0
for i in range(0, n):
  for j in range(i, n):
    if data[i] != data[j]:
      count += 1

print(count)


'''
#2 
'''
