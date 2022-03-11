# 숨바꼭질 - 다익스트라 (비용이 1이기 때문에 BFS 사용 가능!)
import sys
import heapq

input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split())

graph = [[] for _ in range(n+1)]
distance = [INF] * (n+1)

for _ in range(m):
  a, b = map(int, input().split())
  graph[a].append((b, 1))
  graph[b].append((a, 1)) # 양방향 이동 가능

def dijkstra(start): # start = 1
  q = []
  heapq.heappush(q, (0, start))
  distance[start] = 0

  while q:
    dist, now = heapq.heappop(q)
    if dist > distance[now]:
      continue
    # 인접 노드 탐색
    for i in graph[now]:
      cost = dist + i[1]
      if cost < distance[i[0]]:
        distance[i[0]] = cost
        heapq.heappush(q, (cost, i[0]))

dijkstra(1) # 1번 노드부터 시작

max_node = 0
max_dist = 0
result = []
#'전체 맵은 항상 어떤 헛간에서 다른 어떤 헛간으로 도달이 가능한 형태'라는 조건이 주어지기 때문에
# 도달할 수 없는 노드는 없으므로 결과값에는 distance[0] 빼고 INF 값이 없음!
for i in range(1, n+1):
  if max_dist < distance[i]:
    max_dist = distance[i]
    max_node = i
    result = [max_node] # 첫번째로 삽입되는 인덱스(= max_node만을 원소로 갖는 result 리스트 "새로 생성")
  elif max_dist == distance[i]:
    result.append(i) # 이후에 인덱스들 삽입 => 이렇게 하려면 무조건 오름차순으로 정렬되어야 하지 않나?

print(max_node, max_dist, len(result))
    
''' 
# index(), count() 함수를 사용한 간단한 코드
max_val = 0
for i in distance:
  if i != INF:
    max_val = max(max_val, i)

idx = distance.index(max_val)
cnt = distance.count(max_val)
print(idx, max_val, cnt)
'''
# distance : 
# 0 0 1 1 2 2 2