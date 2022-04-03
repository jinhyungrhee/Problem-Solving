from itertools import combinations # 조합 라이브러리 사용

n, m = map(int, input().split())
chicken, house = [], []

for i in range(n):
  data = list(map(int, input().split()))
  for j in range(n):
    if data[j] == 1:
      house.append((i, j)) # 집
    if data[j] == 2:
      chicken.append((i, j)) # 치킨집

# m개의 치킨집 뽑는 조합
candidates = list(combinations(chicken, m))

# 도시 치킨 거리 계산
def get_sum(candidate):
  result = 0
  for hx, hy in house:
    tmp = 987654321 # 위치 주의!
    for cx, cy in candidate:
      tmp = min(tmp, abs(hx - cx) + abs(hy - cy))
    result += tmp
  return result

# 치킨 거리의 합의 최소 찾아서 출력
result = 987654321
for candidate in candidates:
  result = min(result, get_sum(candidate))

print(result)

    

