import sys

INF = int(1e9)
input = sys.stdin.readline

n = int(input()) # 도시의 개수 (1 <= n <= 100)
m = int(input()) # 버스의 개수 (1 <= m <= 100,000)

graph = [[INF] * (n + 1) for _ in range(n + 1)]

# 초기화
for a in range(1, n+1):
  for b in range(1, n+1):
    if a == b:
      graph[a][b] = 0

# 간선 입력받기
for _ in range(m):
  a, b, c = map(int, input().split())
  if graph[a][b] > c: # 같은 도시에 대해 여러 노선이 있는 경우, 더 작은 비용으로 할당
    graph[a][b] = c

# 플로이드 워셜 진행
for k in range(1, n+1):
  for a in range(1, n+1):
    for b in range(1, n+1):
      graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

# 출력
for a in range(1, n+1):
  for b in range(1, n+1):
    if graph[a][b] == INF: # 갈 수 없는 경우, 해당 자리에 0 출력
      print(0, end=" ")
    else:
      print(graph[a][b], end=" ")
  print()