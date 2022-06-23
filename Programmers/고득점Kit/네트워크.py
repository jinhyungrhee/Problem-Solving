from collections import deque

def solution(n, computers):
    answer = 0
    
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    visited = [False for _ in range(n + 1)]
    network = [0 for _ in range(n + 1)] # 네트워크 번호 기록
    graph = [[] for _ in range(n + 1)] # 방문여부 기록
    
    # 인접 행렬을 인접 리스트로 변환
    for i in range(len(computers)):
        for j in range(len(computers)):
            if not i == j and computers[i][j] == 1:
                graph[i+1].append(j+1)
    
    def bfs(graph, start, visited):
        queue = deque([start])
        visited[start] = True
        while queue:
            v = queue.popleft()
            network[v] = start
            # print(v, end=" ")
            for i in graph[v]:
                if not visited[i]:
                    queue.append(i)
                    visited[i] = True
    
    # 방문하지 않은 노드에 대해서만 bfs 수행
    # 방문하지 않은 노드면 새로운 번호 할당하여 network 배열에 기록
    for i in range(1, n + 1):
        if not visited[i]:
            bfs(graph, i, visited)
    
    # network 배열에 최종 기록된 가지수 출력 
    network = set(network) - set(range(1))
    answer = len(network)
    return answer