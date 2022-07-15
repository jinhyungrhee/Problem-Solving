import sys
n = int(sys.stdin.readline())

data = [
  list(map(int, sys.stdin.readline().split()))
  for _ in range(n)
]

dp = [[0]*3 for _ in range(n)]

dp[0][0] = data[0][0]
dp[0][1] = data[0][1]
dp[0][2] = data[0][2]

for i in range(1, n):
  for j in range(3):
    if j == 0: # [i][1]과 [i][2] 비교
      dp[i][j] = min(dp[i-1][1], dp[i-1][2]) + data[i][j]
    elif j == 1: # [i][0]과 [i][2] 비교
      dp[i][j] = min(dp[i-1][0], dp[i-1][2]) + data[i][j]
    elif j == 2: # [i][0]과 [i][1] 비교
      dp[i][j] = min(dp[i-1][0], dp[i-1][1]) + data[i][j]

print(min(dp[n-1]))