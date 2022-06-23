# 주요 조건 : numbers의 원소는 0 이상 1000 이하임 ***
def solution(numbers):
    answer = ''
    data = list(map(str, numbers)) # ['3', '30', '34', '5', '9']
    # print(data) 
    data.sort(key=lambda x:x*3, reverse=True)
    return str(int(''.join(data)))
    
    '''
    data1 = sorted(data, reverse=True)
    print(data1) # ['9', '5', '34', '30', '3']
    print() 
    
    data2 = [elem * 2 for elem in data]
    print(data2) # ['33', '3030', '3434', '55', '99']
    data2.sort(reverse=True)
    print(data2) # ['99', '55', '3434', '33', '3030']
    print()
    
    data3 = [elem * 3 for elem in data]
    print(data3) # ['333', '303030', '343434', '555', '999']
    data3.sort(reverse=True)
    print(data3) # ['999', '555', '343434', '333', '303030']
    
    return answer
    '''
    # Q) *2와 *3은 동일한 정렬 결과를 보이는데 정답에서도 동일할까?
    # A) 세자리 수 원소가 나올 경우에는 *3을 해줘야 정확한 사전식 비교가 가능함!!


# 순열 이용한 방법 => 시간 초과
'''
from itertools import permutations
def solution(numbers):
    answer = ''
    str_num = list(map(str, numbers))
    data = list(map(''.join, permutations(str_num, len(numbers))))
    answer = max(data)
    return answer
'''