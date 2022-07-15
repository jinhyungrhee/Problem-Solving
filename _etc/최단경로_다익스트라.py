# 최단 경로 알고리즘1 - Dijkstra Algorithm
# : 특정한 노드에서 출발하여 다른 노드로 가는 각각의 최단 경로를 구해주는 알고리즘 (음의 간선 X)
# : 그리디 알고리즘 (매번 가장 비용이 적은 노드를 선택해서 임의의 과정을 반복)
# : 실제로 한 번 선택된 노드는 최단 거리가 감소하지 않음 -> 한 단계당 하나의 노드에 대한 최단 거리를 확실히 찾는 것!
# <과정>
  # 1) 출발 노드를 설정
  # 2) 최단 거리 테이블 초기화(0, INF)
  # 3) 방문하지 않은 노드 중, 최단 거리가 가장 짧은 노드 선택
  # 4) 선택된 노드를 거쳐 다른 노드로 가는 비용을 계산하여 최단 거리 테이블 갱신 [Greedy]
  # 5) '3번', '4번' 과정 반복

# =================================================== 구현 ===============================================================
# 구현1(쉽지만 느린 코드 -> O(V^2)) : 최단 거리 노드 매번 선형 탐색, 노드 개수 5,000개 이하에 적합
import sys
input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split())
start = int(input())
graph = [[] for _ in range(n+1)] # 인접 리스트
visited = [False for _ in range(n+1)]
distance = [INF for _ in range(n+1)]

for _ in range(m):
  # a노드에서 b노드로 가는 비용c
  a, b, c = map(int, input().split())
  graph[a].append((b, c))

# 방문하지 않은 노드 중, 가장 최단 거리가 짧은 노드의 번호 반환
def get_smallest_node():
  min_value = INF
  index = 0
  for i in range(1, n+1):
    if distance[i] < min_value and not visited[i]:
      min_value = distance[i]
      index = i
  return index

def dijkstra(start):
  # 시작 노드 초기화
  distance[start] = 0
  visited[start] = True
  # 시작 노드의 인접 노드 거리 초기화
  for v in graph[start]:
    distance[v[0]] = v[1]
  
  # 시작 노드 제외한 노드(n-1개)에 대해 반복
  for i in range(n-1):
    # 현재 최단 거리가 가장 짧은 노드를 꺼내 방문 처리 (매번 선형 탐색 -> O(V^2))
    now = get_smallest_node()
    visited[now] = True
    # 현재 노드와 연결된 다른 노드 확인
    for v in graph[now]:
      cost = distance[now] + v[1]
      # 현재 노드를 거쳐서 다른 노드로 이동하는 거리가 기존 거리보다 더 짧은 경우
      if cost < distance[v[0]]:
        distance[v[0]] = cost  # 갱신

# 다익스트라 수행
dijkstra(start)

# 모든 노드에 대한 최단 거리 출력
for i in range(1, n+1):
  if distance[i] == INF: # 도달할 수 없는 경우
    print("INFINITY")
  else:
    print(distance[i])

# =========================================================================================================================
# 구현2(복잡하지만 빠른 코드 -> O(ElogV))** : 최단 거리 정보 '힙(Heap)'에서 관리, 가장 거리가 짧은 노드 '로그 시간'에 탐색!
# (N = 1,000,000(백만) / logN = 20)
import heapq, sys
input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split())
start = int(input())
graph = [[] for _ in range(n+1)]
distance = [INF for _ in range(n+1)] # visited 역할도 함께 수행


for _ in range(m):
  a, b, c = map(int, input().split())
  graph[a].append((b, c))

def dijkstra(start):
  q = []
  # 시작 노드로 가기 위한 최단 경로는 0으로 설정 후 큐에 삽입 : (거리, 노드) 순서 ***
  heapq.heappush(q, (0, start))
  distance[start] = 0
  while q:
    dist, now = heapq.heappop(q) # 힙큐에서 최단 거리가 가장 짧은 노드 꺼냄
    # 현재 노드가 이미 처리된 적이 있으면 스킵**(visited 대신 사용, 큐에 저장된 거리보다 최단 거리 배열의 거리가 이미 더 짧으면 스킵)
    if distance[now] < dist:
      continue
    # 현재 노드와 연결된 인접 노드 확인
    for v in graph[now]: # 그래프 튜플 : (인접노드, 거리) 순서 ***
      cost = dist + v[1]
      # 현재 노드를 거쳐 다른 노드로 이동하는 것이 기존 거리보다 더 짧은 경우
      if cost < distance[v[0]]:
        distance[v[0]] = cost # 갱신
        # 갱신된 정보 힙에 추가
        heapq.heappush(q, (cost, v[0]))

# 다익스트라 수행
dijkstra(start)

# 최단 거리 출력
for i in range(1, n+1):
  if distance[i] == INF: # 도달할 수 없는 경우
    print("INFINITY")
  else:
    print(distance[i])





