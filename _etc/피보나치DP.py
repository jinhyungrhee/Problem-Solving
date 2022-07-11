# Top-Down 방식(재귀) : O(N)

dp_td = [0] * 100  # "memoization"

def fibo_td(x):
  # 호출 함수 확인
  # print('f(' + str(x) + ')', end=' ')
  
  # 종료조건 (x==1 or 2일 때 1 반환)
  if x == 1 or x == 2:
    return 1

  # 이미 계산된 문제면 그대로 반환
  if dp_td[x] != 0:
    return dp_td[x]

  # 아직 계산되지 않은 문제라면 '점화식'에 따라 피보나치 결과 반환(저장)
  dp_td[x] = fibo_td(x - 1) + fibo_td(x - 2)
  return dp_td[x]

print(fibo_td(99))

# ======================================================================

# Bottom-Up 방식(반복문) => 좀 더 효율적이고 전형적인 방식!

dp_bu = [0] * 100 # "DP 테이블"

# 첫 번째, 두 번째 피보나치 수 초기화
dp_bu[1] = 1
dp_bu[2] = 1

# 찾고자 하는 번째의 수
n = 99 

for i in range(3, n + 1):
  dp_bu[i] = dp_bu[i - 1] + dp_bu[i - 2]

print(dp_bu[n])