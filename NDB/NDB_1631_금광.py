for tc in range(int(input())):
  n, m = map(int, input().split())
  # 금광 정보 (일단 하나의 리스트로 받음)
  array = list(map(int, input().split()))

  # DP 테이블 초기화(array를 그대로 2차원 리스트로 만듦)
  dp = []
  index = 0
  for i in range(n):
    dp.append(array[index:index + m])
    index += m

  # DP 수행
  for j in range(1, m):
    for i in range(n):
      # 왼쪽 위에서 오는 경우
      if i == 0:
        left_up = 0
      else:
        left_up = dp[i-1][j-1]
      # 왼쪽 아래에서 오는 경우
      if i == n-1:
        left_down = 0
      else:
        left_down = dp[i+1][j-1]
      # 왼쪽에서 오는 경우
      left = dp[i][j-1]
      # 세 경우 모두 합치기
      dp[i][j] = dp[i][j] + max(left_up, left_down, left)

  # 출력
  result = 0
  for i in range(n):
    result = max(result, dp[i][m - 1]) # 각 행의 맨 오른쪽 열에 가장 큰 값이 저장됨
        
  print(result)

# 점화식 : dp[i][j] = array[i][j] + max(dp[i-1][j-1], dp[i][j-1], dp[i+1][j-1])

'''my solution

for tc in range(int(input())):
  n, m = map(int, input().split())

  given_seq = list(map(int, input().split()))

  dp = []
  for i in range(1, n+1):
    dp.append(given_seq[m*(i-1):m*(i)])

  for j in range(1, m):
    for i in range(n):
      if i == 0: # 맨 윗 행
        dp[i][j] = dp[i][j] + max(dp[i][j - 1], dp[i + 1][j - 1])
      elif i == n - 1: # 맨 아래 행
        dp[i][j] = dp[i][j] + max(dp[i][j - 1], dp[i - 1][j - 1])
      else:
        dp[i][j] = dp[i][j] + max(dp[i][j - 1], dp[i + 1][j - 1], dp[i - 1][j - 1])

  max_val = 0
  for i in range(n):
    max_val = max(max(dp[i]), max_val)

  print(max_val)
'''