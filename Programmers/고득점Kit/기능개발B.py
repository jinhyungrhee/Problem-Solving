from collections import deque
import math

def solution(progresses, speeds):
    answer = []
    left = [100 - x for x in progresses]
    # 소요시간 미리 계산
    result = [math.ceil(a / b) for a, b in zip(left, speeds)]
    # case1 : [7, 3, 9]
    # case2 : [5, 10, 1, 1, 20, 1]
    
    # front : 가장 오래걸린 소요 시간 인덱스
    front = 0
    
    for idx in range(len(result)): # idx : 0 1 2 || idx : 0 1 2 3 4 5
        if result[idx] > result[front]: # idx == 2 || idx == 1(10), 4(20) 
            answer.append(idx - front) # 2 || 1(1 - 0), 3(4 - 1)  
            # front에 가장 오래걸린 소요 시간 인덱스 저장
            front = idx # front : 2 || front : 1, 4 
    
    # 나머지 남아있는 것 출력
    answer.append(len(result) - front) # 1 (3 - 2) / 2 (6 - 4)
    
    return answer