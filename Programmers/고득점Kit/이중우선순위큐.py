import heapq

def solution(operations):
    answer = [0, 0]
    min_heap = [] # 최소값을 가져와서 max_heap에서 제거
    max_heap = [] # 최대값을 가져와서 min_heap에서 제거
    
    for operation in operations:
        
        op, val = operation.split(" ")
        
        if op == 'I':
            heapq.heappush(min_heap, int(val))
            heapq.heappush(max_heap, -1*int(val))
        elif op == 'D':
            if len(min_heap) == 0:
                continue
            if val == '1': # 최댓값 삭제
                max_val = heapq.heappop(max_heap)
                min_heap.remove(-1 * max_val)
            elif val == '-1': # 최솟값 삭제
                min_val = heapq.heappop(min_heap)
                max_heap.remove(-1 * min_val)
            
        # print(min_heap)
        # print(max_heap)
    
    if len(min_heap) != 0:
        answer[0] = -heapq.heappop(max_heap)
        answer[1] = heapq.heappop(min_heap)

        
    return answer