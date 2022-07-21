n = int(input())

dp = [0] * (n + 1)

# 0번째, 1번째 초기화 -> 있으나마나!
# dp[0] = 0
# dp[1] = 0

# <정답>
for i in range(2, n+1):
  dp[i] = dp[i-1] + 1
  if i % 2 == 0:
    dp[i] = min(dp[i], dp[i // 2] + 1)
  if i % 3 == 0:
    dp[i] = min(dp[i], dp[i // 3] + 1)

# 결과1 
# (n = 10)
# [0, 0, 1, 1, 2, 3, 2, 3, 3, 2, 3]
# (n = 2)
# [0, 0, 1]

# <오답>
# for i in range(2, n + 1):
#   if i % 2 == 0:
#     dp[i] = min(dp[i-1], dp[i//2]) + 1
#   elif i % 3 == 0:
#     dp[i] = min(dp[i-1], dp[i//3]) + 1
#   else:
#     dp[i] = dp[i - 1] + 1

# 결과2 
# (n = 10)
# [0, 0, 1, 1, 2, 3, 2, 3, 3, 2, 3]
# (n = 2)
# [0, 0, 1]
    
# print(dp)
print(dp[n])
