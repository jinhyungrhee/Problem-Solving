# logN 거듭 제곱 알고리즘

def power(a, b, MOD): # a는 밑, b는 지수
  ret = 1
  while b: # b가 0이 될 때까지 (== b 횟수만큼 수행)
    if b&1: # b의 첫째자리 수가 1이면
      ret = ret * a % MOD
    # b의 첫째자리 수가 1이 아니면
    a = a * a % MOD # 제곱 연산 수행
    b >>= 1 # b를 2로 나눔 (shift 연산 수행)

  return ret

a, b, MOD = map(int, input().split())

print(power(a, b, MOD))