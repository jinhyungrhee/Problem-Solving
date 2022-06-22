# Deque를 이용한 BFS
from collections import deque

def solution(numbers, target):
    answer = 0
    n = len(numbers)
    queue = deque()
    queue.append((numbers[0], 0)) # 양의 부호 시작
    queue.append((-1 * numbers[0], 0)) # 음의 부호 시작
    
    while queue:
        temp, idx = queue.popleft()
        idx += 1
        if idx < n: # 최종 노드까지 도달하지 않았으면
            queue.append((temp + numbers[idx], idx))
            queue.append((temp - numbers[idx], idx))
        else: # 최종 노드에 도달했으면
            if temp == target:
                answer += 1
                
    return answer