def solution(answers):
    answer = []
    one = [1,2,3,4,5] # 5
    two = [2,1,2,3,2,4,2,5] # 8
    three = [3,3,1,1,2,2,4,4,5,5] # 10
    cnt_one, cnt_two, cnt_three = 0, 0, 0
    for i in range(len(answers)): # 0 1 2 3 4 5 6 7 8 9 
        if one[i % len(one)] == answers[i]:
            cnt_one += 1
        
        if two[i % len(two)] == answers[i]:
            cnt_two += 1
            
        if three[i % len(three)] == answers[i]:
            cnt_three += 1

    max_val = max(cnt_one, cnt_two, cnt_three)
    if max_val == cnt_one:
        answer.append(1)
    if max_val == cnt_two:
        answer.append(2)
    if max_val == cnt_three:
        answer.append(3)
    
    return answer
