# 1. Stack 사용 => 가장 효율적
# 값이 작아진 경우에만 스택에 남아있는 이전 값들을 비교하는 방식
def solution(prices):
    n = len(prices)
    answer = [i for i in range(n - 1, -1, -1)] # answer을 각 자리의 최대값으로 초기화
    
    # 주식 가격이 떨어지는 경우 찾기
    stack = [0] # 인덱스 관리
    
    for i in range(1, n):
        # stack 안에 값이 존재하면서 stack top(인덱스)의 값보다 다음 값이 "작을 동안" 계속 반복
        # => stack에 넣어 놓은 값보다 다음 값들이 계속 작으면
        while stack and prices[stack[-1]] > prices[i]:
            j = stack.pop() # 스택 top 인덱스(큰 값의 인덱스)를 꺼내서 
            # '현재 인덱스(i)와 가장 큰 값의 인덱스(j)의 차'를 구함 ***
            answer[j] = i - j # 해당 차이를 answer배열에 저장
        
        stack.append(i)
            
    return answer

# 2.완전탐색
'''
def solution(prices):
    answer = [0 for _ in range(len(prices))] 
    
    for i in range(len(prices)):
        for j in range(i+1, len(prices)):
            tmp = 0
            if prices[i] <= prices[j]:
                answer[i] += 1
            else:
                answer[i] += 1
                break
                
    return answer
'''

# 3. Queue 사용
# Queue를 순회하면서 '값이 작아지기 전까지 초를 증가시키는 것'을 Queue가 빌 때까지 반복
'''
from collections import deque
def solution(prices):
    answer = []
    queue = deque(prices)
    
    while queue:
        price = queue.popleft()
        sec = 0
        for q in queue:
            sec += 1
            if price > q:
                break
                
        answer.append(sec)
    return answer 
'''    