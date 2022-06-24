from collections import deque
def solution(begin, target, words):
    answer = 0
    q = deque()
    q.append([begin, 0]) # 단어와 이동횟수
    visited = [False for _ in range(len(words))]
    while q:
        word, cnt = q.popleft()
        if word == target: # 종료 조건
            answer = cnt
            break
        for i in range(len(words)):
            tmp_cnt = 0
            if not visited[i]:
                for j in range(len(word)):
                    # 단어 다른 부분 count
                    if word[j] != words[i][j]:
                        tmp_cnt += 1
                if tmp_cnt == 1:
                    q.append([words[i], cnt + 1])
                    visited[i] = True
    
    return answer

# 내 답안 : (40/100)
'''
from collections import deque
def solution(begin, target, words):
    global str_n
    answer = 0
    n = len(words)
    str_n = len(words[0])
    visited = [False for _ in range(n)]
    step = [0 for _ in range(n)]
    BFS(words[0], words, visited, step)
    
    try:
        t_idx = words.index(target)
        # print(step[t_idx])
        answer = step[t_idx]
    except ValueError:
        return 0
    
    return answer


def BFS(begin, words, visited, step):
    b_idx = words.index(begin)
    visited[b_idx] = True
    step[b_idx] += 1
    queue = deque([b_idx])
    
    while queue:
        now = queue.popleft()
        for i in range(len(words)):
            if not visited[i]:
                if words[i] != words[now] and check_word(words[i], words[now]) == 1:
                    visited[i] = True
                    step[i] = step[now] + 1
                    queue.append(i)
            
            
def check_word(str1, str2):
    count = 0
    for i in range(str_n):
        if str1[i] != str2[i]:
            count += 1
    return count
'''