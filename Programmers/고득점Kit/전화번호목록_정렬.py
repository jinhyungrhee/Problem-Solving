# 정렬(sort) 사용
def solution(phone_book):
    # IDEA : 우선 정렬한 뒤, 앞 뒤로 접두사 관계인지 파악(하나라도 있으면 False리턴하면 되기 때문)
    answer = True
    phone_book.sort()
    
    for i in range(1, len(phone_book)):
        if (phone_book[i].startswith(phone_book[i - 1])):
            answer = False
    
    # zip()을 사용하여, 하나 간격을 두고 비교하는 방법
    # for p1, p2 in zip(phone_book, phone_book[1:]):
    #     if p2.startswith(p1):
    #         answer = False
    
    return answer