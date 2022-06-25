# 이분탐색 : 총 가능한 심사 시간을 이분 탐색함
def solution(n, times):
    answer = []
    left = 1
    right = max(times) * n # 한 심사대에서 모든 사람을 심사할 때 드는 시간(maximum)
    
    while left <= right:
        
        mid = (left + right) // 2 # 중간 지점의 소요 시간 선택 (임시 소요 시간)
        
        people = 0
        for t in times:
            people += mid // t # 임시 소요 시간을 각 심사대 심사 시간으로 나누면 각 심사대에서 심사한 사람 수가 도출됨
            if people >= n: # 모든 심사대를 안 거쳐도 사람 수가 충족되면 후보가 될 수 있음**
                break 
                
        if people >= n: # 심사인원이 충분하면, **답을 갱신**하고 심사 시간 줄임!
            answer = mid
            right = mid - 1
        else: # 심사인원이 부족하면, 심사 시간을 늘림!
            left = mid + 1
            
    return answer