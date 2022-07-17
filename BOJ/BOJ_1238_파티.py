import sys, heapq, copy
input = sys.stdin.readline
INF = int(1e9)

n, m, x = map(int, input().split())

graph = [[] for _ in range(n+1)]
# distance = [0] * (n+1)

for _ in range(m):
  a, b, c = map(int, input().split())
  graph[a].append((b, c)) # g : (노드, 거리)

def dijkstra(start):
  q = []
  heapq.heappush(q, (0, start)) # h : (거리, 노드)
  distance[start] = 0

  while q:
    dist, now = heapq.heappop(q)
    # 방문 여부 체크
    if distance[now] < dist:
      continue
    # 인접 노드 체크
    for v in graph[now]:
      cost = dist + v[1]
      # 현재 노드를 거쳐가는 거리가 기존 거리보다 짧으면 갱신
      if cost < distance[v[0]]:
        distance[v[0]] = cost
        # 갱신 내용 힙에 저장
        heapq.heappush(q, (cost, v[0]))

# x마을에서 돌아오는 최단 거리 구하기
distance = [INF for _ in range(n+1)]
dijkstra(x)
back_distance = copy.deepcopy(distance)

max_value = 0
for i in range(1, n+1):
  distance = [INF for _ in range(n+1)] 
  dijkstra(i) # 1 2 3 4
  # result = x로 가는 거리 + x에서 돌아오는 거리
  result = distance[x] + back_distance[i]
  if max_value < result:
    max_value = result
print(max_value)