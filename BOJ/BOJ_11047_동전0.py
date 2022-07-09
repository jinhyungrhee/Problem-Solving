import sys

n, k = map(int, sys.stdin.readline().split())

coins = []
for _ in range(n):
  coins.append(int(sys.stdin.readline().rstrip()))

count = 0
for i in range(len(coins)-1, -1, -1):
  if k >= coins[i]:
    count += k // coins[i]
    k = k % coins[i]

print(count)


''' 시간초과 => 이중 while문 때문인듯
import sys
n, k = map(int, sys.stdin.readline().split())

coins = []
for _ in range(n):
  coins.append(int(sys.stdin.readline().rstrip()))

# print(coins)
idx = len(coins) - 1
count = 0
while k > 0:
  if coins[idx] <= k:
    while k >= coins[idx]:
      k -= coins[idx]
      count += 1
  idx -= 1

print(count)
'''