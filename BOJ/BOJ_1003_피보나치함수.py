# Bottom-Up (반복문) 방식

dp = [0] * 41 # DP 테이블

# 0번, 1번 초기화
dp[0] = (1, 0)
dp[1] = (0, 1)

tc = int(input())
for _ in range(tc):
  # 찾을 번째의 수
  n = int(input())
  
  for i in range(2, n + 1):
    dp[i] = (dp[i -1][0] + dp[i - 2][0], dp[i -1][1] + dp[i - 2][1])
  
  print(*dp[n])
