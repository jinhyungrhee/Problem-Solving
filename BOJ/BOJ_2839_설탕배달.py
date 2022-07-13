# Bottom-Up 방식의 DP

n = int(input())
INF = 1e9
dp = [INF] * 5001

dp[3] = 1
dp[5] = 1

for i in range(6, 5001):
  dp[i] = min(dp[i-3], dp[i-5]) + 1

# print(dp)
# print(dp[n])
if dp[n] >= INF:
  print(-1)
else:
  print(dp[n])

# 반례
# n = 7의 경우,
# d[7] = min(dp[3], dp[4]) + 1 == min(1000000000.0, 1000000000.0) + 1 = 1000000001.0이 됨
# 따라서 if dp[n] == INF(1000000000.0): 조건에 걸리지 않음
# 해당 예외를 처리하기 위해서 if dp[n] >= INF: 로 변경