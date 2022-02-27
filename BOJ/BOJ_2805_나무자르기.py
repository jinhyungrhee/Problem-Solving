import sys

n, m = list(map(int, sys.stdin.readline().split()))

array = list(map(int, sys.stdin.readline().split()))

start = 0
end = 999999999 # max(array) 대신 입력조건의 최대치 사용 => O(1)

result = 0
while start <= end:

  mid = (start + end) // 2 # mid가 곧 절단기의 높이

  sum_val = 0
  for i in array:
    if i > mid :
      sum_val += i - mid
  
  # sum_val이 m보다 크면 절단기를 높이고 (= 더 적게 추출)
  # sum_val이 m보다 작으면 절단기를 낮춤 (= 더 많이 추출)
  if sum_val >= m:
    # mid(=h)가 최대가 되어야 하므로 늘렸을 때 결과값을 반환
    result = mid
    start = mid + 1
  else:
    end = mid - 1

print(result)