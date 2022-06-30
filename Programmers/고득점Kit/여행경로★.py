def solution(tickets):
    # dict 자료구조를 이용한 인접 리스트 생성 *** 
    route = dict()
    for ticket in tickets:
        if ticket[0] in route:
            route[ticket[0]].append(ticket[1])
        else:
            route[ticket[0]] = [ticket[1]] # 리스트로 추가해야 다음번에 append가 가능함!
    print(route)
    
    for key in route.keys():
        # 다음 갈 곳이 알파벳 순서상 앞서야 하므로 값들을 내림차순 정렬함
        route[key].sort(reverse=True) 
        
    # DFS 수행
    stack = ['ICN']
    path = []
    while stack:
        top = stack[-1]
        # 특정 공항에서 출발하는 표가 없거나 티켓을 다 써버린 경우
        if top not in route or len(route[top]) == 0:
            path.append(stack.pop())
        else:
            # 특정 공항에서 출발하는 표가 존재하는 경우
            stack.append(route[top].pop())
            
    return path[::-1] # 뒤에서 부터 출력