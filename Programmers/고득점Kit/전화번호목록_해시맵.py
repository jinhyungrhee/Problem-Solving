def solution(phone_book):
    answer = True
    hash_map = {}
    
    for phone_num in phone_book:
        hash_map[phone_num] = 1
        
    # 접두어가 hash map에 존재하는지 찾음
    for phone_num in phone_book:
        # jubdoo는 매 번호마다 새롭게 초기화 됨
        jubdoo = ""
        for num in phone_num: # 1 / 11 / 119
            jubdoo += num
            if jubdoo in hash_map and jubdoo != phone_num: # 자기 번호와는 달라야 함
                answer = False
        
    return answer