# 1.스택을 Queue처럼 사용한 경우

# bridge 리스트와, truck_weights 리스트를 큐처럼 사용(pop(0), append())
# Queue를 사용하면 맨 앞만 확인하면 되므로 인덱스 따로 관리할 필요 없음 ***
def solution(bridge_length, weight, truck_weights):
    
    answer = 0 # 경과시간
    bridge = [0 for _ in range(bridge_length)] # 다리 위 상황 표시 큐(빈곳은 0으로 표시**)
    
    while bridge:
        
        answer += 1
        bridge.pop(0) # 다음 트럭이나 빈 공간(트럭이 못 올라올 경우)을 올리기 위해 공간 하나 만듦
        
        if truck_weights: # 트럭 대기열에 트럭이 존재할 경우에만(-> 없으면 계속 빼내기만 하면 됨)
            
            if sum(bridge) + truck_weights[0] <= weight: # 현재 상태에서 트럭을 올릴 수 있다면
                # 트럭 추가
                t = truck_weights.pop(0)
                bridge.append(t)
            else: # 현재 트럭을 올릴 수 없는 상황이라면
                # 빈 공간 추가
                bridge.append(0)
            
        
    return answer

# 2.Queue 자료구조 두 개를 사용한 경우 => 시간초과 발생
'''
from collections import deque
def solution(bridge_length, weight, truck_weights):
    
    answer = 0 # 경과 시간
    bridge = deque([0 for _ in range(bridge_length)])
    truck_weights = deque(truck_weights)
    
    while bridge:
        answer += 1
        bridge.popleft()
        
        if truck_weights:
            if sum(bridge) + truck_weights[0] <= weight:
                t = truck_weights.popleft()
                bridge.append(t)
            else:
                bridge.append(0)
    
    return answer
'''

# 3. bridge만 Queue로 사용할 경우 => 시간초과 발생
'''
from collections import deque
def solution(bridge_length, weight, truck_weights):
    
    answer = 0 # 경과 시간
    bridge = deque([0 for _ in range(bridge_length)])
    # truck_weights = deque(truck_weights)
    
    while bridge:
        answer += 1
        bridge.popleft()
        
        if truck_weights:
            if sum(bridge) + truck_weights[0] <= weight:
                t = truck_weights.pop(0)
                bridge.append(t)
            else:
                bridge.append(0)
    
    return answer
'''
# 4. truck_weights만 Queue로 사용한 경우 => 통과
'''
from collections import deque
def solution(bridge_length, weight, truck_weights):
    
    answer = 0 # 경과 시간
    # bridge = deque([0 for _ in range(bridge_length)]) # 새로운 bridge를 생성하고 초기화하면서 deque로 만드는 것이 시간이 오래 걸리는 듯 ** 
    bridge = [0 for _ in range(bridge_length)]
    truck_weights = deque(truck_weights) # 기존에 존재하는 리스트를 deque로 바꾸는 것은 꽤 빨리 이루어지는 듯 **
    
    while bridge:
        answer += 1
        bridge.pop(0)
        
        if truck_weights:
            if sum(bridge) + truck_weights[0] <= weight:
                t = truck_weights.popleft()
                bridge.append(t)
            else:
                bridge.append(0)
    
    return answer
'''
    