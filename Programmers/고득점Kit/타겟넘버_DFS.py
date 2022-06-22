# 재귀를 이용한 DFS(backtracking)
def solution(numbers, target):
    answer = 0 # 전역변수가 아닌 지역변수
    n = len(numbers)
    
    def dfs(idx, result):
        if idx == n:
            if result == target:
                nonlocal answer # 지역변수를 전역변수처럼 사용
                answer += 1
            return # 마지막 차수까지 도달했으므로 리턴
        else:
            dfs(idx + 1, result + numbers[idx]) # 먼저 더하기를 진행한 다음
            dfs(idx + 1, result - numbers[idx]) # return 되어 나왔을 때 빼기 진행 (backtrack)
            
    dfs(0, 0)
    
    return answer