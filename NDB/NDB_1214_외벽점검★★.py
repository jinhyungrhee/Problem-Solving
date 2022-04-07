# 완전탐색, 순열 사용
from itertools import permutations

def solution(n, weak, dist):
    # 원형을 일자 형태로 변경(길이 2배)
    length = len(weak)
    for i in range(length):
        weak.append(weak[i] + n)
    # 투입할 친구수의 최솟값 찾기 (len(dist) + 1로 초기화)
    answer = len(dist) + 1
    
    for start in range(length):
        # 각 시작점에서 친구를 나열하는 모든 경우의 수 확인(순열)
        for friends in list(permutations(dist, len(dist))):
            count = 1
            position = weak[start] + friends[count - 1]
            
            # 시작점부터 모든 취약 지점 확인
            for index in range(start, start + length):
                # 점검 가능한 위치 벗어나면 친구 한 명더 투입
                if position < weak[index]:
                    count += 1
                    # 더 이상 투입이 불가능하면 종료
                    if count > len(dist): 
                        break
                    position = weak[index] + friends[count - 1]
            
            # 최솟값 계산
            answer = min(answer, count)
        
    if answer > len(dist):
        return -1
    return answer