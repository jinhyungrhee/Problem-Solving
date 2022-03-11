import sys

input = sys.stdin.readline
INF = int(1e9)

n = int(input())

graph = [[INF] * (n+1) for _ in range(n+1)]

grid = [
  list(map(int, input().split()))
  for _ in range(n)
]

# 주의) 자기 자신으로 가는 비용을 0으로 해주면 안됨!
# for i in range(1, n+1):
#   for j in range(1, n+1):
#     if i == j:
#       graph[i][j] = 0

# 간선 정보 - 유/무
for i in range(n):
  for j in range(n):
    if grid[i][j] == 1:
      graph[i+1][j+1] = grid[i][j]


# 플로이드 워셜 알고리즘 수행
for k in range(1, n+1):
  for a in range(1, n+1):
    for b in range(1, n+1):
      graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])


for a in range(1, n+1):
  for b in range(1, n+1):
    if graph[a][b] == INF:
      print(0, end=" ")
    else:
      print(1, end=" ")
  print()
      