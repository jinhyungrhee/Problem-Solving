from itertools import permutations

def solution(numbers):
    answer = 0
    
    data = list(numbers)

    # 순열로 종이조각으로 만들 수 있는 경우의 수 모두 구함(순서가 의미가 있으므로 순열 사용)**
    temp = []
    for i in range(1, len(numbers) + 1):
        temp += list(permutations(data, i))
    
    # 순열로 구해진 튜플을 unpacking하여 num 리스트에 저장 (=> join 함수 사용)**
    num = []
    for t in temp:
        # << join() : 리스트(튜플) 내의 문자열을 합치는 함수 >> ***
        # print(t) # ('1',) , ('7',) , ('1', '7'), ('7', '1')
        # print(''.join(t)) # 1, 7, 17, 71
        num.append(int(''.join(t)))
    # 또는
    # num = [int(''.join(t)) for t in temp]    
    
    num = list(set(num))
    # print(num)
    
    for n in num:
        if is_prime(n):
            answer += 1
    
    return answer

def is_prime(num):
    if num < 2:
        return False
    
    # 에라토스테네스 체 응용
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    
    # 나눠지는 수가 없다면 그것이 바로 소수
    return True