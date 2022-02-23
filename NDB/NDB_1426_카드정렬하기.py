import heapq

n = int(input())

deck = []

for i in range(n):
  heapq.heappush(deck, int(input()))

cmp_count = 0
while len(deck) != 1:
  a = heapq.heappop(deck)
  b = heapq.heappop(deck)
  sum_value = (a + b)
  cmp_count += sum_value
  heapq.heappush(deck, sum_value)

print(cmp_count)

'''입력 예제
4
10
20
40
50

round1 :
10 + 20 = 비교 30
round2 :
30 + 40 = 비교 70
round3 :
50 + 70 = 비교 120

힙에 원소가 하나만 남으면 while문 종료
'''