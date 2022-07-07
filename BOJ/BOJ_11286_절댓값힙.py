import heapq, sys

n = int(sys.stdin.readline())

heap = []
for _ in range(n):
  num = int(sys.stdin.readline())
  if num == 0:
    if len(heap) == 0:
      print(0)
    else:
      min_val = heapq.heappop(heap)
      print(min_val[1])
  else:
    heapq.heappush(heap, (abs(num), num))