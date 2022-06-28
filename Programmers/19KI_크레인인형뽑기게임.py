def solution(board, moves):
    answer = 0
    n = len(board)
    stack = [[] for _ in range(n)]
    bucket = [0]
    
    # N x N 격자를 각각의 stack으로 변경 
    for i in range(n):
        for j in range(n):
            if board[i][j] != 0:
                stack[j].append(board[i][j])
    
    count = 0
    for m in moves:
        if stack[m-1]:
            num = stack[m-1].pop(0)
            # print(num)
            if bucket[-1] != num:
                bucket.append(num)
            else:
                bucket.pop()
                count += 2
    
    answer = count
    return answer