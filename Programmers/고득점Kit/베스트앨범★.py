
def solution(genres, plays):
    answer = []
    G = {} # {장르 : 총 재생 횟수}
    T = {} # {장르 : [(재생 횟수 , 고유 번호)] }
    
    # 사전 초기화
    for i in range(len(genres)):
        genre = genres[i]
        play = plays[i]
        G[genre] = G.get(genre, 0) + play
        T[genre] = T.get(genre, []) + [(play, i)] 
        
    print(G)
    print(T)
    
    # 1. 재생횟수 기준으로 장르별 내림차순 정렬 => G 사전 정렬
    # items() : 딕셔너리의 원소를 tuple 형태로 변환
    G = sorted(G.items(), key=lambda x:x[1], reverse=True) 
    print(G)
    
    # 2. 정렬된 장르별로 순회하면서 전체 정렬 => G 사전의 key를 순서대로 사용하여 T 사전의 value 정렬
    # **[핵심]은 G사전과 T사전의 key가 동일하다는 점!!** => 여러 가지 기준으로 동시에 정렬할 수 있음!!!
    for genre, _ in G: # pop, classic 순서
        T[genre] = sorted(T[genre], key=lambda x:x[0], reverse=True) # pop인 것 먼저 재생횟수 내림차순 순으로 정렬한 뒤 
        answer += [idx for (play, idx) in T[genre][:2]] # 상위 두개 정답 배열에 인덱스 저장 (그 다음에 classic 진행)
    
    return answer