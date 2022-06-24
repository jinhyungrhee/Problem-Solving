def solution(begin, target, words):
    answer = 0
    stack = [begin]
    visited = [False for _ in range(len(words))]
    
    if target not in words:
        return 0
    
    while stack:
        word = stack.pop()
        if word == target:
            return answer # DFS로 타고 내려간 깊이 리턴
        
        for i in range(len(words)):
            tmp_cnt = 0
            if not visited[i]:
                for j in range(len(word)):
                    if word[j] != words[i][j]:
                        tmp_cnt += 1
                
                if tmp_cnt == 1:
                    visited[i] = True
                    stack.append(words[i])
        answer += 1
    
    return answer