# 편집거리 -> '최소 편집 거리'를 계산해 이차원 배열로 저장!
# '왼쪽 열에 저장된 문자'(sunday)를 '위쪽 행에 있는 문자'(saturday)로 변경하는 비용 계산
# ex) dp[3][3] : 'sun'을 'sat'으로 바꾸기 위한 최소 편집 거리 == 2

def solution(text1, text2):
  
  row_size = len(text1)
  col_size = len(text2)

  # dp 초기화
  dp = [[0] * (col_size + 1) for _ in range(row_size + 1)]

  for i in range(1, col_size + 1):
    dp[0][i] = i

  for j in range(1, row_size + 1):
    dp[j][0] = j

  # dp 테이블 채우기
  for i in range(1, row_size + 1):
    for j in range(1, col_size + 1):
      if text1[i-1] == text2[j-1]: # 문자가 같은 경우
        dp[i][j] = dp[i-1][j-1]
      else: # 문자가 다른 경우
        dp[i][j] = 1 + min(dp[i][j-1], dp[i-1][j], dp[i-1][j-1]) # 삽입(왼쪽), 삭제(위쪽), 교체(왼쪽 위) 중 최소비용 + 1

  return dp[row_size][col_size]

a = input()
b = input()

print(solution(a, b))