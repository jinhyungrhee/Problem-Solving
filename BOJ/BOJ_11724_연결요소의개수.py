from collections import deque
import sys

n, m = map(int, sys.stdin.readline().split())

# 인접리스트
graph = [[] for _ in range(n+1)]
visited = [False for _ in range(n+1)]

for _ in range(m):
  s, e = map(int, sys.stdin.readline().split())
  graph[s].append(e)
  graph[e].append(s)

def BFS(node):
  q = deque([])
  q.append(node)
  visited[node] = True

  while q:
    curr = q.popleft()
    for v in graph[curr]:
      if not visited[v]:
        visited[v] = True
        q.append(v)
  
count = 0
for i in range(1, n + 1):
  if not visited[i]:
    BFS(i)
    count += 1

print(count)