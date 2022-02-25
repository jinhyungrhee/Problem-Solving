n, c = list(map(int, input().split()))

array = []

for _ in range(n):
  array.append(int(input()))

array.sort()

start = 1 # 가능한 최소 거리(min gap)
end = array[-1] - array[0] # 가능한 최대 거리(max gap)
result = 0

while(start <= end):
  # mid는 가장 인접한 두 공유기 사이의 거리(gap)
  mid = (start + end) // 2
  value = array[0]
  count = 1
  # 현재의 mid값을 이용해 공유기 설치
  for i in range(1, n): # 앞에서부터 차근차근 설치
    if array[i] >= value + mid: # 이전에 선택된 집과 gap을 더한 값보다 다음집의 값이 크면 update
      value = array[i]
      count += 1
  
  # c개 이상의 공유기를 설치할 수 있는 경우 -> 거리 증가
  if count >= c:
    start = mid + 1
    # 거리 증가했을 때 최적의 결과를 저장(parametric search)
    result = mid
  # c개 이상의 공유기를 설치할 수 없는 경우 -> 거리 감소
  else:
    end = mid - 1

print(result)

'''
TIP:
- 이진탐색으로 '가장 인접한 두 공유기 사이의 거리'를 조절해가며, 
  매 순간 실제로 공유기를 설치하여 C보다 많은 개수로 공유기를 설치할 수 있는지 체크!

- 다만, '가장 인접한 두 공유기 사이의 거리'의 최댓값을 찾아야 하므로, C보다 많은 개수로 공유기를 설치할 수 있다면 
  '가장 인접한 두 공유기 사이의 거리'의 값을 증가시켜서, 더 큰 값에 대해서도 성립하는지 체크하기 위해 다시 탐색 수행!
'''