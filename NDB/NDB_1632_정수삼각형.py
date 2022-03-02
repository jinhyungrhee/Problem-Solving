n = int(input())

array = []
for _ in range(n):
  array.append(list(map(int, input().split())))

dp = [[0] * n for _ in range(n)]

dp[0][0] = array[0][0]

for i in range(1, n):
  dp[i][0] = dp[i-1][0] + array[i][0]
  dp[i][i] = dp[i-1][i-1] + array[i][i]

# dp 수행 (2행부터 채움)
for i in range(2, n):
  for j in range(1, i+1): # dp[2][1]
    dp[i][j] = max(dp[i-1][j-1], dp[i-1][j]) + array[i][j]

print(max(dp[n-1])) # 마지막 행에서의 최대값 출력


# 더 간결한 코드 (array 변수 사용하지 않고 바로 dp테이블 만들기) => 이 경우, **범위 체크** 필요!
'''
n = int(input())
dp = []

for _ in range(n):
  dp.append(list(map(int, input().split())))

# DP 수행 => 두번째 줄부터 내려가면서 확인
for i in range(1, n):
  for j in range(i+1):
    # ** 범위 체크 **
    # '왼쪽 위'에서 내려오는 경우
    if j == 0:
      up_left = 0
    else:
      up_left = dp[i-1][j-1]
    # '바로 위'에서 내려오는 경우
    if j == i:
      up = 0
    else:
      up = dp[i-1][j]
    # 최대 합 저장
    dp[i][j] = dp[i][j] + max(up_left, up)

print(max(dp[n-1])) # 마지막 행에서의 최대값 출력
'''