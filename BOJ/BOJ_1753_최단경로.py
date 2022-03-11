import sys
import heapq

input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split())
start = int(input())

graph = [[] for _ in range(n + 1)] # 인접 노드 그래프
distance = [INF] * (n + 1) # 최소 거리 정보 (시작점에서부터 각 노드 까지)

for _ in range(m):
  u, v, w = map(int, input().split())
  graph[u].append((v, w)) # i[0]은 목적 노드, i[1]은 가중치

def dijkstra(start):
  q = []
  heapq.heappush(q, (0, start)) # 첫번째 인덱스(=가중치) 기준으로 정렬
  distance[start] = 0 # 자기 자신까지의 거리는 0

  while q:
    dist, now = heapq.heappop(q) # (초기) 0 1
    # 이미 처리된 노드 skip
    if dist > distance[now]: # (초기) 0 > 0 => False
      continue
    # 인접 노드 탐색
    for i in graph[now]:
      cost = dist + i[1] # 인접 노드로 가는 "새로운 경로값"
      if cost < distance[i[0]]: # 인접 노드로 가는 기존 경로값보다 "새로운 경로값"이 작으면 갱신
        distance[i[0]] = cost
        heapq.heappush(q, (cost, i[0]))

dijkstra(start)

# 시작점에서부터 각 정점으로까지의 최단 경로 값 출력
for i in range(1, n+1):
  if distance[i] == INF:
    print("INF")
  else:
    print(distance[i])