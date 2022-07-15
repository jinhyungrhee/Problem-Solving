import heapq, sys
input = sys.stdin.readline
INF = int(1e9)
n = int(input())

graph = [[] for _ in range(n+1)]
# distance = [INF for _ in range(n+1)]

for _ in range(n):
  tmp = list(map(int, input().split()))
  target, data = tmp[0], tmp[1:]
  for i in range(0, len(data) - 1, 2):
    graph[target].append((data[i], data[i+1])) # 그래프:(노드, 거리) 순서

# print(graph)

def dijkstra(start):
  q = []
  heapq.heappush(q, (0, start)) # 힙큐:(거리, 노드) 순서
  distance[start] = 0

  while q:
    dist, now = heapq.heappop(q)
    # 이미 방문한 노드이면 skip
    if distance[now] < dist:
      continue

    # 인접 노드 탐색 
    for v in graph[now]: # (노드, 거리) 순서
      cost = dist + v[1]
      # 현재 노드를 거쳐 가는 거리가 기존 거리보다 짧으면 갱신
      if cost < distance[v[0]]:
        distance[v[0]] = cost
        # 갱신된 정보 힙큐에 저장
        heapq.heappush(q, (cost, v[0]))

# 1번 노드에서 다익스트라 한 번 실행
distance = [INF for _ in range(n+1)]
dijkstra(1)
max_node = distance.index(max(distance[1:])) # 최단 거리가 가장 긴 노드 

# 최단 거리가 가장 긴 노드에서 다익스트라 한 번 더 실행
distance = [INF for _ in range(n+1)]
dijkstra(max_node)
print(max(distance[1:]))

# IDEA : 최단거리 알고리즘 두 번 실행하는 이유
# -> 리프에서 루트까지의 거리 중에서 최대 거리가 '트리의 지름(=최장 거리)'이 아닌 경우가 있을 수 있음! (첫 번째 최단 거리 알고리즘)
# -> 즉, 리프에서 리프의 거리 중에서 '트리의 지름(=최장 거리)'이 있는 경우 고려해야 함! (두 번째 최단 거리 알고리즘)
# (https://www.acmicpc.net/board/view/92776)

# PS. DFS를 두 번 사용해도 답을 구할 수 있을 듯!(한번 해보기)