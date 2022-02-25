def check(array, start, end):
  if start > end:
    return None

  mid = (start + end) // 2 # 중간점
  
  # 중간점 인덱스가 array 값과 동일한지 확인
  if array[mid] == mid:
    return mid
  # (오름차순 정렬된 리스트이므로)
  # 중간점 인덱스가 array 값보다 크면 -> 오른쪽 탐색
  elif array[mid] < mid:  
    return check(array, mid + 1, end)
  # 중간점 인덱스가 array 값보다 작으면 -> 왼쪽 탐색
  else:
    return check(array, start, mid - 1)


n = int(input())
array = list(map(int, input().split()))

result = check(array, 0, n - 1)
if result == None:
  print(-1)
else:
  print(result)
