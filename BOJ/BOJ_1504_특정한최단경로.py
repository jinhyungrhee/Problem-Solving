import sys, heapq
input = sys.stdin.readline
INF = int(1e9)

n, e = map(int, input().split())

graph = [[] for _ in range(n+1)]
# distance = [INF for _ in range(n+1)]

for _ in range(e):
  a, b, c = map(int, input().split())
  graph[a].append((b, c)) # 그래프는 (노드, 거리) 순서
  graph[b].append((a, c))

# print(graph)

def dijkstra(start):
  q = []
  heapq.heappush(q, (0, start)) # 힙큐는 (거리, 노드) 순서
  distance[start] = 0

  while q:
    # print(q)
    # 힙큐에서 현재 노드 출력 : (거리, 노드) 순
    dist, now = heapq.heappop(q)
    # 이미 방문한 노드(=이미 최단거리가 구해진 노드)면 skip 
    if distance[now] < dist:
      continue
    # 인접 노드 탐색
    for v in graph[now]: # 그래프는 (노드, 거리) 순서
      cost = dist + v[1]
      # 현재 노드를 거쳐가는 거리가 기존 거리보다 짧으면 갱신
      if cost < distance[v[0]]:
        distance[v[0]] = cost
        # 힙큐에 갱신된 정보 저장
        heapq.heappush(q, (cost, v[0]))

u, v = map(int, input().split())

# result1 : u-v 순서로 이동
result1 = 0

distance = [INF for _ in range(n+1)]
dijkstra(1)
result1+= distance[u]

distance = [INF for _ in range(n+1)]
dijkstra(u)
result1 += distance[v]

distance = [INF for _ in range(n+1)]
dijkstra(v)
result1 += distance[n]


# result2 : v-u 순서로 이동
result2 = 0

distance = [INF for _ in range(n+1)]
dijkstra(1)
result2+= distance[v]

distance = [INF for _ in range(n+1)]
dijkstra(v)
result2 += distance[u]

distance = [INF for _ in range(n+1)]
dijkstra(u)
result2 += distance[n]

# result1(u-v순서)과 result2(v-u순서)를 비교하여 더 짧은 것을 결과로 지정
if result1 < result2:
  result = result1
else:
  result = result2

# 결과가 INF보다 크면 이동할 수 없는 것임!
if result >= INF:
  print(-1)
else:
  print(result)