# Queue(FIFO) 사용
# '입출력 순서'에 대한 언급 有 -> 스택 또는 큐, pop() 사용
def solution(progresses, speeds):
    answer = []
    time = 0
    count = 0
    
    # pop(0)을 사용하여 리스트를 마치 큐처럼 사용(popleft())***
    while len(progresses) > 0:
        # 출시 가능하면 큐에서 제거(pop(0))
        if (progresses[0] + time * speeds[0]) >= 100:
            progresses.pop(0)
            speeds.pop(0)
            # 개발 완료 수 1 증가
            count += 1
        else: # 아직 출시 불가능한 경우
            if count > 0: # 이전 개발 완료 기록이 있으면 ***
                answer.append(count) # 바로 이전까지 출시 가능했던 것들(개수) answer에 기록
                count = 0 # 새로 기록하기 위해 초기화 
            # 소요되는 날짜를 증가시킴
            time += 1
    
    answer.append(count) # 마지막에 남아있던 것 까지 기록
    
    return answer