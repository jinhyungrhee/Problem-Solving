# 병사 배치하기 == 최대 증가 부분 수열(LIS) 문제
# d[i] = 'array[i]를 마지막 원소로 가지는 부분 수열의 최대 길이'라고 할 때,
# 점화식 : d[i] = max(d[i], d[j] + 1) if array[j] < array[i] (0 <= j < i)

n = int(input())

array = list(map(int, input().split()))
# 가장 긴 감소 부분 수열 문제로 reverse
array.reverse()

# 1차원 dp 테이블
dp = [1] * n

for i in range(1, n):
  for j in range(0, i):
    if array[j] < array[i]:
      dp[i] = max(dp[i], dp[j] + 1) # dp[i]에 계속 값이 갱신됨
  
# 열외시켜야 하는 병사의 최소 수 (= 전체 길이 - 최장 감소 부분 수열의 길이)
print(n - max(dp))
