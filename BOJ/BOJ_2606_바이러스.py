n = int(input())
m = int(input())

graph = [[] for _ in range(n + 1)]
visited = [False for _ in range(n + 1)]

for _ in range(m):
  s, e = map(int, input().split())
  graph[s].append(e)
  graph[e].append(s)

def DFS(node):

  global count
  visited[node] = True
  

  for v in graph[node]:
    if not visited[v]:
      count += 1
      DFS(v)

count = 0
DFS(1)
print(count)