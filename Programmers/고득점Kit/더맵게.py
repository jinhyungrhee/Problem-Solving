import heapq
def solution(scoville, K):

    heap = []
    for i in scoville:
        heapq.heappush(heap, i)
    # print(heap)
    
    count = 0
    while heap[0] < K:
        try:
            heapq.heappush(heap, heapq.heappop(heap) + (heapq.heappop(heap) * 2))
            count += 1
        except IndexError: # 만약 남아있는 인덱스가 없어서 에러가 발생하면 -1 리턴
            return -1
            
    return count