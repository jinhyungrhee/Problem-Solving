# 이진 탐색 사용
import sys

n = int(sys.stdin.readline())

array = list(map(int, sys.stdin.readline().split()))

array.sort()

m = int(sys.stdin.readline())

req = list(map(int, sys.stdin.readline().split()))

def binary_search(array, target, start, end):

  while start <= end:
    
    mid = (start + end) // 2

    if array[mid] == target:
      return mid

    elif array[mid] > target: # 왼쪽 탐색
      end = mid - 1
    else: # 오른쪽 탐색
      start = mid + 1

  # 모두 탐색했는데 없으면 None 리턴
  return None
      
for x in req:
  result = binary_search(array, x, 0, n - 1)
  if result == None:
    print(0)
  else:
    print(1)

''' set 자료형 사용
import sys

n = int(sys.stdin.readline())

array = set(list(map(int, sys.stdin.readline().split())))

m = int(sys.stdin.readline())

cmp = list(map(int, sys.stdin.readline().split()))

for elem in cmp:
  if elem in array:
    print(1)
  else:
    print(0)
'''

'''
입력 조건에 '모든 정수의 범위는 -2^31 보다 크거나 같고 2^31보다 작다.'가 있으므로 계수 정렬(Counting Sort)은 사용 불가
'''