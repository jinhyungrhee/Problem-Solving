def solution(n, lost, reserve):
    answer = 0
    # 전처리 과정 필요
    # 여벌 체육복을 가져온 학생이 체육복을 도난 당할 수 있음 -> 결국 여벌이 없는 것이나 마찬가지
    # 이 경우, lost나 reverse에 중복으로 존재하는 요소들 모두 삭제해줌 (set:'차집합 연산'을 통한 중복 제거)
    set_reserve = set(reserve) - set(lost)
    set_lost = set(lost) - set(reserve)
    
    for i in set_reserve:
        if i - 1 in set_lost: # 왼쪽 먼저 탐색
            set_lost.remove(i - 1)
        elif i + 1 in set_lost: # 그 다음 오른쪽 탐색
            set_lost.remove(i + 1)
    return n - len(set_lost)
    
    # 오답
    '''
    for i in lost: # 2 4
        print(i)
        prev_ = i - 1
        # print(prev_)
        next_ = i + 1
        if (prev_ in reserve):
            lost.remove(i)
            reserve.remove(prev_)
    answer = n - len(lost)
    
    return answer
    '''
    