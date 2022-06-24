def solution(brown, yellow):
    answer = []
    
    total = brown + yellow
    
    for b in range(1, total+1): # 1부터 N까지 탐색 : 시간복잡도 O(2N) == O(N)
        a = total // b # 가능한 a와 b에 대하여
        if a >= b: # 조건1 check
            if 2*a + 2*b == brown + 4 and (a-2) * (b-2) == yellow: # 조건2, 조건3 check
                return [a, b]
    
    return answer 

''' 내 답 (76.9 / 100)
def solution(brown, yellow):
    answer = []
    
    N = brown + yellow
    divisor = []
    divisor_back = []
    
    get_divisor(yellow, divisor, divisor_back)
    print(divisor, divisor_back)
    
    for i in range(len(divisor)):
        if (divisor[i] + 2) * (divisor_back[i] + 2) == N:
            # print(divisor[i] + 2, divisor_back[i] + 2)
            answer = [divisor_back[i] + 2, divisor[i] + 2]
    
    return answer

def get_divisor(n, divisor, divisor_back):
    n = int(n)
    
    if n == 1:
        divisor_back.append(1)
    
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            divisor.append(i) # 나눈 수 저장
            if i != n//i : 
                divisor_back.append(n//i) # 나누어 떨어진 수 저장    
'''