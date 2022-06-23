from collections import deque

def solution(priorities, location):
    answer = 0
    
    queue = deque()
    
    for i in range(len(priorities)):
        queue.append((priorities[i], i)) # (중요도, 인덱스)
    # 또는
    # queue = deque([(v, i) for i, v in enumerate(priorities)])
    
    
    while len(queue):
        
        item = queue.popleft()

        if queue and max(queue)[0] > item[0]: # 더 큰 값이 존재하면 뒤로 보냄
            queue.append(item)
        else: # 가장 큰 값이면 출력
            answer += 1 # '순서' 값 증가시킴
            if item[1] == location: # 원하는 item이 출력될 때의 '순서'   
                break        
    
    return answer