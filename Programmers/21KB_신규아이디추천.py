def solution(new_id):
    answer = ''
    # 1단계
    new_id = new_id.lower()
    
    # 2단계
    for i in new_id:
        if not i.isalpha() and not i.isdigit() and i != '-' and i != '_' and i != '.':
            new_id = new_id.replace(i, '')
    
    # 3단계 -> 2개인 것을 1개가 될 때까지 replace (while)
    while new_id.find('..') != -1:
        new_id = new_id.replace('..', '.')
        
    # 4단계
    if new_id[0] == '.' or new_id[-1] == '.':
        new_id = new_id.strip('.') # 양쪽 끝. 삭제
        
    # 5단계
    if len(new_id) == 0:
        new_id = "a"
    
    # 6단계
    if len(new_id) >= 16:
        new_id = new_id[:15]
        if new_id[-1] == '.':
            new_id = new_id.rstrip('.')
    
    # 7단계
    if len(new_id) <= 2:
        c = new_id[-1]
        while len(new_id) < 3:
            new_id += c
        
    # print(new_id)
    answer = new_id
    return answer