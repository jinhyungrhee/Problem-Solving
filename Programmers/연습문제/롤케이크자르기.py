from collections import defaultdict

def solution(topping):
    answer = 0
    older = defaultdict(int)
    for elem in topping:
        older[elem] += 1
    younger = set()
    
    while len(topping) != 0:
        temp = topping.pop()
        if older[temp] != 0:
            older[temp] -= 1
        if older[temp] == 0:
            del older[temp]
        younger.add(temp)
        if len(older) == len(younger):
            answer += 1
    
    return answer