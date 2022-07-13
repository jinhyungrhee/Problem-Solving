import sys
from collections import deque
n = int(sys.stdin.readline())
INF = 1e9

# 인접 리스트
graph = [[] for _ in range(n+1)]
dist = [0 for _ in range(n+1)]

for _ in range(n-1):
  s, e = map(int, sys.stdin.readline().split())
  graph[s].append(e)
  graph[e].append(s)

def BFS(node):
  q = deque([])
  dist[node] = 1
  q.append(node)

  while q:
    curr = q.popleft()
    for v in graph[curr]:
      if dist[v] == 0:
        dist[v] = dist[curr] + 1
        q.append(v)

BFS(1)
# print(graph)
# print(dist)

result = ''
for i in range(2, len(graph)):
  min_val = INF
  print_val = 0
  for j in range(len(graph[i])):
    if min_val > dist[graph[i][j]]:
      min_val = dist[graph[i][j]]
      print_val = graph[i][j]
  result += str(print_val) + '\n'

print(result[:-1])

# IDEA :BFS로 각 노드의 최단 거리(dist)를 찾고, 인접리스트를 순회하며 "인접노드 중 가장 최단 거리가 짧은 노드"(=그것이 곧 부모노드)를 출력!