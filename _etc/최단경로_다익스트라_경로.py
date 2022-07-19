# IDEA : 최단 거리 갱신 시 prev 리스트(prev[현재노드])에 이전 노드(now)만 저장하면 됨!
import sys, heapq
input = sys.stdin.readline
INF = int(1e9)

n = int(input())
m = int(input())

graph = [[] for _ in range(n+1)]
distance = [INF for _ in range(n+1)]
prev = [-1 for _ in range(n+1)] # 이전 노드를 저장하기 위한 리스트 (-1로 초기화) **

for _ in range(m):
  a, b, c = map(int, input().split())
  graph[a].append((b, c)) # g : (노드, 거리)

def dijkstra(start):
  q = []
  distance[start] = 0
  heapq.heappush(q, (0, start)) # h : (거리, 노드)

  while q:
    dist, now = heapq.heappop(q)
    # 방문 여부 체크
    if distance[now] < dist:
      continue
    # 인접 노드 탐색
    for v in graph[now]:
      cost = dist + v[1]
      if cost < distance[v[0]]:
        distance[v[0]] = cost
        prev[v[0]] = now # 이전 노드 기록 **
        heapq.heappush(q, (cost, v[0])) 

s, e = map(int, input().split())
dijkstra(s)

print(distance)
print(prev)