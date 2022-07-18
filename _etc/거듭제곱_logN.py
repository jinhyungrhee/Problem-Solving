# Project Euler P.48
# 1^1 + 2^2 + 3^3 + ... + 10^10 = 10405071317이다.
# 1^1 + 2^2 + 3^3 + ... + 1000^1000의 마지막 10자리 숫자는 무엇인가?

# 마지막 10자리 숫자는 곧 우리가 나눠주어야 하는 숫자임!
MOD = int(1e10) # 10의 10승

# [방법1] : 반복문 실행 (O(N^2))
def process1():
  ans1 = 0
  for i in range(1, 1001):
    tmp1 = 1
    for j in range(1, i+1):
      tmp1 = tmp1 * i % MOD # 10의 10승으로 나눈 나머지가 우리가 구할 값임!
    ans1 = (ans1 + tmp1) % MOD

  print(ans1)
process1()

# [방법2] : power() 함수를 직접 작성하여 실행 (O(logN))
# -> built-in pow() 함수를 그대로 돌릴 경우, 301자리(1000^1000) 숫자를 int로 나타낼 수 없음!
# 로직: 모든 자연수(9, 12 등)는 2진수로 표현할 수 있고, 2진수는 한번마다 한자리씩 구할 수 있기 때문에 총 logN만큼의 시간이 걸림!
# ex) a^9 = a * a^8
# ex) a^12 = a^4 * a^8 
# 즉, a^12를 구하는 가장 좋은 방법:
# a
# a^2
# (a^2)^2 = a^4
# ((a^2)^2)^2 = a^8

def power(a, b, MOD): # 밑(a), 지수(b), MOD값( modular를 해줘야 int overflow를 방지할 수 있음)
  ret = 1

  while b: # b번 곱하기 == b가 0이 될 때까지 수행!
    if b&1: # b의 첫번째 자리수가 1이면
      ret = ret * a % MOD
    a = a * a % MOD
    b >>= 1 # b를 2로 나눔

  return ret

def process2():
  ans2 = 0
  for i in range(1, 1001):
    ans2 = (ans2 + power(i, i, MOD)) % MOD # power() : i를 i번 곱해준 값을 MOD로 나눈 값
  print(ans2)

process2()

# 참고1 : https://www.acmicpc.net/board/view/70289
# 참고2 : https://www.youtube.com/watch?v=otu3FCyoUVY