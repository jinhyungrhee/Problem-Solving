def find_parent(parent, x):
  if parent[x] != x:
    parent[x] = find_parent(parent, parent[x])  
  return parent[x]

def union_parent(parent, a, b):
  a = find_parent(parent, a)
  b = find_parent(parent, b)
  if a < b:
    parent[b] = a
  else:
    parent[a] = b

# 각 탑승구를 서로 다른 집합으로 나타냄
# 비행기가 차례대로 들어오면, 가능한 큰 번호의 탑승구로 도킹(=합집합 연산)을 수행한다고 가정
# 단, 집합의 루트가 0이 되면 더 이상 도킹이 불가능함

g = int(input()) # 1 ~ g
p = int(input()) # p대의 비행기

parent = [0] * (g+1)

for i in range(1, g+1):
  parent[i] = i

result = 0
for _ in range(p):
  data = find_parent(parent, int(input())) # 현재 비행기의 탑승구 루트 확인
  if data == 0: # 현재 루트가 0 이면 종료
    break
  # 그렇지 않으면 바로 왼쪽 집합과 합치기
  union_parent(parent, data, data - 1)
  result += 1 # 도킹 횟수 추가

print(result)