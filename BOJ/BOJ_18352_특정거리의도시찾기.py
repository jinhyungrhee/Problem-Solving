import sys, heapq
input = sys.stdin.readline
INF = int(1e9)

n, m, k, x = map(int, input().split())

graph = [[] for _ in range(n+1)]
distance = [INF for _ in range(n+1)]

for _ in range(m):
  a, b = map(int, input().split())
  graph[a].append((b, 1)) # graph : (노드, 거리)


def dijkstra(start):
  q = []
  heapq.heappush(q, (0, start)) # heapq : (거리, 노드)
  distance[start] = 0

  while q:
    dist, now = heapq.heappop(q)
    # 방문한 적이 있으면 skip
    if distance[now] < dist:
      continue
    # 인접노드 탐색
    for v in graph[now]:
      cost = dist + v[1]
      # 현재 노드를 거쳐가는 거리가 기존 거리보다 짧으면 갱신
      if cost < distance[v[0]]:
        distance[v[0]] = cost
        # 갱신된 정보 힙큐에 저장
        heapq.heappush(q, (cost, v[0]))


dijkstra(x)

# print(distance)
is_possible = False
for i in range(1, len(distance)):
  if distance[i] == k:
    is_possible = True
    print(i)

if not is_possible:
  print(-1)


# BFS로도 풀 수 있음!