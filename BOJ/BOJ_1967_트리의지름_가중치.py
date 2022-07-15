import sys, heapq
input = sys.stdin.readline
INF = int(1e9)

n = int(input())

graph = [[] for _ in range(n+1)]
# distance = [INF for _ in range(n+1)]

for _ in range(n-1):
  a, b, c = map(int, input().split())
  graph[a].append((b, c)) # graph : (자식노드, 가중치) 순
  graph[b].append((a, c))


def dijkstra(start):
  q = []
  heapq.heappush(q, (0, start)) # heapq : (가중치, 노드) 순
  distance[start] = 0

  while q:
    dist, now = heapq.heappop(q)
    # 방문 여부 체크
    if distance[now] < dist:
      continue
    # 인접 노드 탐색
    for v in graph[now]:
      cost = dist + v[1]
      # 현재 노드를 거치는 거리가 기존 거리보다 짧으면 갱신
      if cost < distance[v[0]]:
        distance[v[0]] = cost
        # 갱신된 정보 힙큐에 저장
        heapq.heappush(q, (cost, v[0]))

# 루트에서 가장 먼 최단거리 노드(리프노드) 구함
distance = [INF for _ in range(n+1)]
dijkstra(1)
farthest_node = distance.index(max(distance[1:]))

# 위에서 구한 리프노드에서 가장 먼 최단거리 구함
# 루트-리프 보다 거리가 먼 리프-리프가 존재할 수 있기 때문!
distance = [INF for _ in range(n+1)]
dijkstra(farthest_node)
print(max(distance[1:]))