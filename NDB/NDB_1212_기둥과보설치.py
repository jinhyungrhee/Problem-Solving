# def check_col(grid, x, y):
#     return y == 0 or grid[x-1][y] == 1 or grid[x][y] == 1 or grid[x][y-1] == 0

# def check_bo(grid, x, y):
#     return (grid[x-1][y] == 1 and grid[x+1][y] == 1) or grid[x][y-1] == 0 or grid[x+1][y-1] == 0

def possible(answer): # 현재 설치된 구조물이 가능한 구조물인지 체크
    for x, y, stuff in answer:
        if stuff == 0: # 기둥
            if y == 0 or [x - 1, y, 1] in answer or [x, y, 1] in answer or [x, y - 1, 0] in answer:
                continue # 설치 가능
            return False
        elif stuff == 1: # 보
            if [x, y - 1, 0] in answer or [x + 1, y - 1, 0] in answer or ([x - 1, y , 1] in answer and [x + 1, y, 1] in answer):
                continue # 설치 가능
            return False
    return True

def solution(n, build_frame):
    answer = []
    for frame in build_frame:
        x, y, stuff, operate = frame
        if operate == 0: # 삭제
            answer.remove([x, y, stuff]) # 삭제 먼저 진행
            if not possible(answer): # 불가능하면
                answer.append([x, y, stuff]) # 다시 설치
        if operate == 1: # 설치
            answer.append([x, y, stuff]) # 설치 먼저 진행
            if not possible(answer): # 불가능하면
                answer.remove([x, y, stuff]) # 다시 삭제                
    
    return sorted(answer)