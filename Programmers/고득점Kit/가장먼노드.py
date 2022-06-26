from collections import deque # BFS

def solution(n, edge):
    answer = 0
    
    visited = [False for _ in range(n + 1)]
    dist = [0 for _ in range(n + 1)]
    
    graph = [[] for _ in range(n + 1)]
    
    for e in edge:
        graph[e[0]].append(e[1])
        graph[e[1]].append(e[0])
        
    # print(graph)
    BFS(graph, visited, dist, 1)
    
    # print(dist)
    answer = dist.count(max(dist))
    
    
    return answer

def BFS(graph, visited, dist, node):
    q = deque([node])
    visited[node] = True
    
    while q:
        cur = q.popleft()
        for v in graph[cur]:
            if not visited[v]:
                dist[v] = dist[cur] + 1
                visited[v] = True
                q.append(v)