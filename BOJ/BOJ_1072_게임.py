import sys

input = sys.stdin.readline

x, y = map(int, input().split())

z = y * 100 // x # 현재 승률

if z >= 99: # 99% 100%는 아무리 승을 추가해도 더 이상 올라가지 않음(100 99 / 101 100 / 102 101 => 99)
  print(-1)
else:
  start = 1
  end = 1000000000
  #end = x
  result = 0
  
  while start <= end:
  
    mid = (start + end) // 2 # 이긴 판 수
  
    if (mid + y)* 100 // (mid + x) <= z: # 수정된 승률이 현재 승률보다 작거나 같으면, 판수를 늘려야 함(= 오른쪽 탐색)
      start = mid + 1
    else: # 수정된 승률이 현재 승률보다 커지면, 판수를 줄여야 함(=왼쪽 탐색)
      result = mid  # 그 중 최소값을 찾는 것이므로 end를 변경할 때 result 업데이트 (=lower_bound)
      end = mid - 1

  print(result)
