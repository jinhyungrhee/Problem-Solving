# 화성 탐사 - 격자에서의 최소 거리(dx,dy)
# 다익스트라 '우선순위 큐' 사용
import sys
import heapq

input = sys.stdin.readline
INF = int(1e9)

tc = int(input())

def in_range(x, y):
  return 0 <= x < n and 0 <= y < n

# 원래는 이차원 리스트(graph)에서 인접 노드 관리했으나, 격자(grid)에서는 dx-dy 테크닉으로 모든 인접노드의 최소값 갱신
def dijkstra(x, y):
  q = []
  heapq.heappush(q, (grid[x][y], x, y)) # 가장 첫 원소(="비용")를 기준으로 정렬됨
  distance[x][y] = grid[x][y] # distance 리스트의 첫 값은 grid[0][0] 값으로 초기화 ***

  dx = [-1, 1, 0, 0]
  dy = [0, 0, -1, 1]

  while q: # q가 빌 때 까지 반복
    # 가장 작은 값부터 꺼냄
    dist, now_x, now_y = heapq.heappop(q)
    # 이미 처리된 노드는 skip
    if dist > distance[now_x][now_y]:
      continue
    # 인접노드 확인하여 더 작은 값이 있으면 갱신
    for i in range(4):
      nx = now_x + dx[i]
      ny = now_y + dy[i]
      if in_range(nx, ny):
        cost = dist + grid[nx][ny]
        if cost < distance[nx][ny]: # 갱신
          distance[nx][ny] = cost
          heapq.heappush(q, (cost, nx, ny))
          

for _ in range(tc):
  n = int(input())

  grid = [
    list(map(int, input().split()))
    for _ in range(n)
  ]

  distance = [[INF]*n for _ in range(n)]

  dijkstra(0, 0)

  print(distance[n-1][n-1])

  # # distance 리스트 출력
  # for a in range(n):
  #   for b in range(n):
  #     if distance[a][b] == INF:
  #       print(-1, end=" ")
  #     else:
  #       print(distance[a][b], end=" ")
  #   print()