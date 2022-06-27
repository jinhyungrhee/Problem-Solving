def solution(lottos, win_nums):
    answer = []
    n = len(lottos)
    unknown = lottos.count(0)  # 지워진 개수(0의 개수)

    lottos = set(lottos)
    win_nums = set(win_nums)
    
    result = win_nums - lottos
    scored = n - len(result) # 맞은 개수
    
    max_num = unknown + scored
    min_num = scored
    
    # 최고 많이 맞은 개수나 최고 적게 맞은 개수가 1개나 0개면 모두 6등이어야 함
    if max_num < 2:
        max_num = 1
    if min_num < 2:
        min_num = 1
    
    answer = [7 - max_num, 7 - min_num] # 등수로 환산하여 출력
    
    return answer