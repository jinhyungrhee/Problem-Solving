a, b, c = map(int, input().split())

# 결과가 계속 반복되므로 최대 두번만 해보면 됨 (1번 or 2번만 수행)

# 한 번만 수행한 결과(c가 홀수 일 때) : a^b
# 두 번 수행한 결과(c가 짝수 일 때) : (a^b)^b == a (처음과 동일) -> 즉, c가 짝수일 때는 아예 연산을 수행하지 않아도 됨!
for i in range(c%2):
  a ^= b

print(a)

# 동일한 코드
# print(a^b if c%2 else a)
