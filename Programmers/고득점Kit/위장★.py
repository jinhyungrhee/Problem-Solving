def solution(clothes):
    answer = 0
    hash_map = {}
    for clothe, category in clothes:
        # hash_map.get(param1, param2) -> param2 : 만약 찾는 param1이 없으면 param2를 리턴
        hash_map[category] = hash_map.get(category, 0) + 1 # 각 종류별 개수 저장
    
    # print(hash_map)
    
    # 아무 종류의 옷도 입지 않는 경우를 포함한 조합(combination) 계산하기
    answer = 1
    for category in hash_map:
        answer *= (hash_map[category] + 1)
        
    # 아무 종류의 옷도 입지 않은 경우(단 한 가지 경우의 수) 제외시키기
    answer -= 1
    
    return answer