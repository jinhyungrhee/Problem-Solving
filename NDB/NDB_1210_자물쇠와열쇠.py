# 220701 (슈도코드 작성 및 참고)
def rotate(key): # key(이차원 리스트)를 90도 회전
    n = len(key)
    m = len(key[0])
    
    result = [[0]*m for _ in range(n)]
    
    for i in range(n):
        for j in range(m):
            result[j][n-i-1] = key[i][j] # 이차원 리스트 90도 회전 알고리즘
            
    return result

def check(new_lock):
    # new_lock은 확장된 lock에 key 값을 더한 결과(완전탐색 중)
    lock_len = len(new_lock) // 3 # 기존 lock의 길이
    for i in range(lock_len, lock_len * 2):
        for j in range(lock_len, lock_len * 2): # 1/3 ~ 2/3 지점 탐색
            if new_lock[i][j] != 1:
                return False
    return True           

def solution(key, lock):
    n = len(lock)
    m = len(key)
    new_lock = [[0] * n * 3 for _ in range(n * 3)]
    
    for i in range(n):
        for j in range(n):
            new_lock[n + i][n + j] = lock[i][j]
            
    for _ in range(4):
        key = rotate(key)
        for i in range(n * 2):
            for j in range(n * 2):
                for a in range(m):
                    for b in range(m):
                        new_lock[i+a][j+b] += key[a][b] # key 삽입
                # 삽입한 key가 맞는지 확인
                if check(new_lock) == True:
                    return True
                # 맞지 않으면 key 빼기 (backtracking)
                for a in range(m):
                    for b in range(m):
                        new_lock[i+a][j+b] -= key[a][b] # key 제거(원상복구)
    return False

# 220629
''' 내 답(53.0 / 100.0)

def solution(key, lock):
    # answer = True
    
    n = len(key)
    for i in range(4):
        r_key = rotate(key, n)
        key = r_key # 기존 key 갱신
        # print(r_key)
        for x in range(n):
            for y in range(n):
                if check(key, lock, x, y, n): # lock의 x,y를 시작점으로 key와 맞는지 체크
                    return True
    return False


def rotate(key, n):
    r_key = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            r_key[j][n-i-1] = key[i][j]
    return r_key

def check(key, lock, x, y, n):
    # lock에 모든 부분에 대해 key 맞춰보기
    for i in range(n):
        for j in range(n):
            if x + i < n and y + j < n:
                if lock[x + i][y + j] == 0 and key[i][j] == 1:
                    return True
    return False
'''