def solution(phone_book):
    answer = True
    hash_map = {}
    
    for phone_num in phone_book:
        hash_map[phone_num] = 1
        
    # 접두어가 hash map에 존재하는지 찾음 ((p_b)1,000,000 X (p_n)20 => 2천만번)
    for phone_num in phone_book:
        # jubdoo는 매 번호마다 새롭게 초기화 됨
        jubdoo = ""
        for num in phone_num: # 1 / 11 / 119
            jubdoo += num
            # 해쉬맵을 사용하면 for문으로 탐색(O(N))하는 것보다 더 빠른 시간에 탐색 가능(O(1)) ***
            if jubdoo in hash_map and jubdoo != phone_num: # 자기 번호와는 달라야 함
                answer = False
        
    return answer