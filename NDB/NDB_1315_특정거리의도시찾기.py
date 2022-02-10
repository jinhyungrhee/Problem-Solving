from collections import deque

n, m, k, x = map(int, input().split())

graph = [[] for _ in range(n+1)]

for _ in range(m):
  a, b = map(int, input().split())
  graph[a].append(b)

#print("========================")

# 모든 도시에 대한 거리 초기화
dist = [-1] * (n+1)
# 출발 도시까지의 거리는 0으로 설정
dist[x] = 0 

# BFS 수행
q = deque([x])


while q:

  now = q.popleft()
  # 현재 도시에서 이동할 수 있는 모든 도시들을 확인
  for next_node in graph[now]:
    # 아직 방문하지 않은 도시라면
    if dist[next_node] == -1:
      # 최단거리 갱신
      dist[next_node] = dist[now] + 1
      q.append(next_node)

# 최단거리가 k인 모든 도시들의 번호를 오름차순으로 출력
check = False

for i in range(1, n+1):
  if dist[i] == k:
    print(i)
    check = True

# 만약 최단 거리가 K인 도시가 없으면 -1 출력
if check == False:
  print(-1)      

'''
모든 도로의 거리는 1' -> BFS 사용
'''