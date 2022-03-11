# 정확한 순위
import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split()) # n : 학생수(노드 수), m : 성적비교횟수(간선의 수)

# 다익스트라? 플로이드워셜? => 플로이드 워셜 v

# 플로이드 워셜

graph = [[INF] * (n + 1) for _ in range(n + 1)]

for a in range(1, n+1):
  for b in range(1, n+1):
    if a == b:
      graph[a][b] = 0

for _ in range(m):
  a, b = map(int, input().split())
  graph[a][b] = 1 # 성적 : a < b

# 알고리즘 수행
  for k in range(1, n+1):
    for a in range(1, n+1):
      for b in range(1, n+1):
        graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])


# # 좌우 대칭 합치기 => 자기 자신 제외 모든 칸이 채워져 있으면, 정확한 순위 계산 가능
# for a in range(1, n+1):
#   for b in range(1, n+1):
#     if graph[a][b] != INF:
#       graph[b][a] = 0
#       graph[b][a] += graph[a][b]

# # 순위를 정확히 알 수 있는 학생 수 계산
# total = 0
# for i in range(1, n+1):
#   count = 0
#   for j in range(1, n+1):
#     if graph[i][j] != INF and graph[i][j] != 0:
#       count += 1
#   if count == n - 1:
#     total += 1

# print(total)

# ** 위의 내용 더 간단히 작성 가능 **
total = 0
for i in range(1, n+1):
  count = 0
  for j in range(1, n+1):
    if graph[i][j] != INF or graph[j][i] != INF:
      count += 1
  if count == n:
    total += 1

print(total)
      
# 플로이드 워셜 결과 (모든 노드에 대해서 출력):
# 0 2 0 2 1 3 
# 0 0 0 0 0 0 
# 0 2 0 1 0 2 
# 0 1 0 0 0 1 
# 0 1 0 1 0 2 
# 0 0 0 0 0 0 

'''
# 다익스트라

graph = [[] for _ in range(n+1)]
distance = [INF] * (n+1)

# 노드, 간선 입력
for _ in range(m):
  a, b = map(int, input().split())
  graph[a].append((b, 1))

def dijkstra(start):
  q = []
  heapq.heappush(q, (0, start))
  distance[start] = 0 # (1)missing
  
  while q:
    dist, now = heapq.heappop(q)
    if dist > distance[now]:
      continue

    for i in graph[now]:
      cost = dist + i[1]
      if cost < distance[i[0]]: # (2)wrong : 새로운 거리값이 "인접노드 거리값"보다 작으면 갱신 (now노드 X)
        distance[i[0]] = cost # (3)wrong : (now 노드X, now 노드의 "인접노드")
        heapq.heappush(q, (cost, i[0]))

        
# 알고리즘 수행
dijkstra(1)

# 출력
# print(distance)
for i in range(1, n+1):
  if distance[i] == INF:
    print(0, end=" ")
  else:
    print(distance[i], end=" ")

# 다익스트라 결과 : 0 2 0 2 1 3 (1번노드에 대해서만 출력)
'''