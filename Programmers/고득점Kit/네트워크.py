from collections import deque
# IDEA : 네트워크의 개수는 곧 트리의 개수임. 한 노드에서 탐색을 시작해 최대 방문한 것을 1개의 트리로 계산!

# 모범답안 DFS
def solution(n, computers):
    answer = 0
    visited = [False for i in range(n)]
    
    for computer in range(n):
        if not visited[computer]:
            DFS(n, computers, computer, visited)
            answer += 1 # 총 DFS를 수행한 횟수를 체크
            
    return answer

def DFS(n, computers, now, visited):
    visited[now] = True
    for next in range(n):
        # 자신이 아니면서 현재 노드와 연결된 컴퓨터이면서
        if next != now and computers[now][next] == 1:
            if not visited[next]: # 아직 방문하지 않았다면
                DFS(n, computers, next, visited) # DFS 수행

# 모범답안 BFS
def solution(n, computers):
    answer = 0
    
    visited = [False for _ in range(n)]
    
    for computer in range(n):
        if not visited[computer]:
            BFS(n, computers, computer, visited)
            answer += 1 # BFS가 수행된 횟수가 곧 트리(=네트워크)의 개수임
    
    return answer


def BFS(n, computers, now, visited):
    visited[now] = True
    queue = deque([now])
    
    while queue:
        now = queue.popleft()
        for next in range(n): # 인접 노드 탐색
            if now != next and computers[now][next] == 1:
                if not visited[next]:
                    visited[next] = True
                    queue.append(next)


# 내 답안
'''
def solution(n, computers):
    answer = 0
    
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
'''