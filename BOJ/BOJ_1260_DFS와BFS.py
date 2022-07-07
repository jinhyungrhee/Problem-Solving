from collections import deque

n, m, v = map(int, input().split())

graph = [[] for _ in range(n + 1)]

# 인접리스트로 그래프 구성
for _ in range(m):
  s, e = map(int, input().split())
  graph[s].append(e)
  graph[e].append(s)
  
# 정렬을 해야 오름차순 노드로 탐색
for g in graph:
  g.sort()

def DFS(node):
  
  visited[node] = True
  print(node, end=" ")

  for v in graph[node]:
    if not visited[v]:
      DFS(v)

def BFS(node):

  q = deque([])
  q.append(node)
  visited[node] = True
  print(node, end=" ")

  while q:
    curr = q.popleft()
    for v in graph[curr]:
      if not visited[v]:
        q.append(v)
        visited[v] = True
        print(v, end=" ")
  

visited = [False] * (n + 1)
DFS(v)

print()

visited = [False] * (n + 1)
BFS(v)