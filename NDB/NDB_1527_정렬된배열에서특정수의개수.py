# 이진 탐색 사용
# 시작 인덱스, 끝 인덱스를 구하는 이진 탐색 함수 두 개 작성(**고급 테크닉**)

# 정렬된 수열에서 값이 x인 원소의 개수를 세는 메서드
def count_by_value(array, x):

  n = len(array)

  # x가 처음 등장한 인덱스 계산
  a = first(array, x, 0, n - 1)

  # 수열에 x가 존재하지 않는 경우
  if a == None:
    return 0 # "0개" 리턴

  # x가 마지막으로 등장한 인덱스 계산
  b = last(array, x, 0, n - 1)

  # 개수 반환
  return b - a + 1

# 처음 위치를 찾는 이진 탐색 메서드(재귀)
def first(array, target, start, end):
  
  if start > end: # 종료 조건
    return None

  mid = (start + end) // 2
  
  # 해당 값을 가지는 원소 중에서 가장 왼쪽에 있는 경우에만 인덱스 변환 ***
  # (mid 바로 전 값이 target보다 작은 값이면서 mid가 target 값인 경우)
  # 또는 (mid가 맨 처음 값이면서 target 값인 경우)
  if (mid == 0 or target > array[mid - 1]) and array[mid] == target:
    return mid
  # 중간점의 값보다 찾고자 하는 값이 작거나 **같은** 경우 -> 왼쪽으로 계속 내려감
  elif array[mid] >= target:
    return first(array, target, start, mid - 1)
  # 중간지점의 값보다 찾고자 하는 값이 큰 경우 -> 오른쪽 확인
  else:
    return first(array, target, mid + 1, end)

# 마지막 위치를 찾는 이진 탐색 메서드(재귀)
def last(array, target, start, end):

  if start > end:
    return None

  mid = (start + end) // 2

  # 해당 값을 가지는 원소 중에서 가장 오른쪽에 있는 경우만 인덱스 변환 ***
  # (mid 바로 다음 값이 target보다 큰 값이면서 mid가 target 값인 경우)
  # 또는 (mid가 맨 마지막 값이면서 target 값인 경우)
  if (mid == n-1 or target < array[mid + 1]) and array[mid] == target:
    return mid
  # 중간 지점의 값보다 찾고자 하는 값이 크거나 **같은** 경우 -> 오른쪽으로 계속 올라감
  elif array[mid] <= target:
    return last(array, target, mid + 1, end)
  # 중간 지점의 값보다 찾고자 하는 값이 작은 경우 -> 왼쪽 확인
  else:
    return last(array, target, start, mid - 1)


n, target = list(map(int, input().split()))

data = list(map(int, input().split()))

cnt = count_by_value(data, target)

if cnt == 0:
  print(-1)
else:
  print(cnt)


'''bisect 사용
from bisect import bisect_left, bisect_right

n, target = list(map(int, input().split()))

data = list(map(int, input().split()))

def count_by_range(a, left_value, right_value):
  left_index = bisect_left(a, left_value)
  right_index = bisect_right(a, right_value)

  return right_index - left_index

result = count_by_range(data, target, target)

if result == 0:
  print(-1)
else:
  print(result)
'''