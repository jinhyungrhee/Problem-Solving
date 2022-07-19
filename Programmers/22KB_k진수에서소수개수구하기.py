import math

# 10진수 -> N진수
def n_ary(n, q):
    rev_base = ''
    while n > 0:
        n, mod = divmod(n ,q)
        rev_base += str(mod)
    return rev_base[::-1]

def solution(n, k):
    target = n_ary(n, k)
    tmp = target.split('0')
    
    # 에라토스테네스의 체
    count = 0
    for t in tmp:
        if t == '':
            continue
        is_prime = True
        for i in range(2, int(math.sqrt(int(t)))+1):
            if int(t) % i == 0:
                is_prime = False
        if int(t) != 1 and is_prime:
            count += 1
    
    return count