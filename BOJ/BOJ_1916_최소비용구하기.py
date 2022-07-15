import sys, heapq
input = sys.stdin.readline
INF = int(1e9)

n = int(input())
m = int(input())

graph = [[] for _ in range(n+1)]
distance = [INF for _ in range(n+1)]

for _ in range(m):
  a, b, c = map(int, input().split())
  graph[a].append((b, c)) # graph : (노드, 거리) 순

s, e = map(int, input().split())

def dijkstra(start):
  q = []
  heapq.heappush(q, (0, start)) # heapq : (거리, 노드) 순
  distance[start] = 0

  while q:
    dist, now = heapq.heappop(q)
    # 방문 여부 체크
    if distance[now] < dist:
      continue
    # 인접 노드 탐색
    for v in graph[now]:
      cost = dist + v[1]
      # 현재 노드 거쳐가는 거리가 기존 거리보다 짧으면 갱신
      if cost < distance[v[0]]:
        distance[v[0]] = cost
        # 갱신된 정보 힙에 저장
        heapq.heappush(q, (cost, v[0]))


dijkstra(s)

print(distance[e])