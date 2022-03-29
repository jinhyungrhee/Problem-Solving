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

n, m = map(int, input().split())
parent = [0] * n

# 모든 간선을 담을 리스트와 최종 비용 변수
edges = []
total_sum = 0
result = 0

# 부모 테이블 초기화
for i in range(n):
  parent[i] = i

for _ in range(m):
  x, y, cost = map(int, input().split())
  # 비용순으로 정렬하기 위해
  edges.append((cost, x, y))

# 간선을 '비용'순으로 오름차순 정렬
edges.sort()

for edge in edges:
  cost, a, b = edge
  total_sum += cost
  # 사이클이 발생하지 않는 경우에만 집합에 포함
  if find_parent(parent, a) != find_parent(parent, b):
    union_parent(parent, a, b)
    result += cost

print(total_sum - result)