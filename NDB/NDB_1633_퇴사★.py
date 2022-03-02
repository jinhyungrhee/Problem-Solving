# 거꾸로 확인하는 방식의 다이나믹 프로그래밍
# => 뒤쪽부터 매 상담에 대하여 "현재 상담 일자의 이윤(p[i]) + 현재 상담을 마친 일자부터의 최대 이윤(dp[t[i] + i])"
# 예) 1일 차에 상담 진행하는 경우 최대 이익 : 1일 차의 상담 금액 + 4일부터의 최대 상담 금액

# dp[i] = "i번째 날부터 마지막 날까지 낼 수 있는 최대 이익"일 때,
# 점화식 : dp[i] = max(p[i] + dp[t[i] + i], max_value) (max_value는 뒤에서부터 계산할 때 '현재까지의 최대 상담 금액')

n = int(input())
t = [] # 각 일별 상담기간
p = [] # 상담 금액
dp = [0] * (n + 1)
max_val = 0

# 입력
for _ in range(n):
  x, y = map(int, input().split())
  t.append(x)
  p.append(y)

# print(t)
# print(p)

# 뒤에서부터 DP 수행
for i in range(n - 1, -1, -1):
  time = t[i] + i # time은 '끝나는 일자'
  if time <= n: # 상담이 퇴사 전에 끝나면
    # 점화식에 따라 최대 이익 계산
    dp[i] = max(p[i] + dp[time], max_val)
    max_val = dp[i]
  else: # 상담이 퇴사 이후까지 계획되어 있으면
    dp[i] = max_val

# print(dp)
print(max_val)