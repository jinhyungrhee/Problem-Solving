def solution(people, limit):
    cnt = 0
    people.sort()
    
    i = 0
    j = len(people) - 1
    
    while i <= j:
        
        # 가장 무거운 사람과 가벼운 사람을 태운 것이 
        if people[i] + people[j] <= limit:
            i += 1 # limit을 넘지 않으면 둘 다 태우고

        j -= 1 # limit을 넘을 경우 무거운 사람만 태움
        cnt += 1
    
    return cnt

'''
def solution(people, limit):
    answer = 0
    people.sort()
    i = 0
    j = len(people) - 1
    
    while i <= j:
        # 가장 큰 사람과 작은 사람의 합과 limit 비교
        if people[i] + people[j] > limit: # limit을 넘으면
            j -= 1 # 큰 사람 한 명만 태움
        else:
            # 둘 다 태움
            i += 1
            j -= 1
        answer += 1
    
    return answer
'''