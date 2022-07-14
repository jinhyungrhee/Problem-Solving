# 50 / 100

import sys
n = int(sys.stdin.readline()) # n : O의 개수, n+1 : I의 개수
m = int(sys.stdin.readline()) # s의 길이
s = sys.stdin.readline().rstrip()

target = ''
jarisu = n + (n + 1)

for i in range(jarisu):
  if i % 2 == 0:
    target += 'I'
  else:
    target += 'O'

print(jarisu, target)

count = 0
for i in range(0, len(s) - jarisu + 1): # M
  print(s[i:i + jarisu])
  if s[i:i+jarisu] == target: # (2N + 1)
    count += 1

# 총 시간 복잡도 : O(N*M)

print(count)

# =====================================================================
# 100 / 100

import sys
n = int(sys.stdin.readline()) # n : O의 개수, n+1 : I의 개수
m = int(sys.stdin.readline()) # s의 길이
s = sys.stdin.readline().rstrip()

count = 0
p_count = 0 # 'IOI' 단위로 패턴이 등장했는지 파악
idx = 1

# *** while을 사용해야만 하는 이유 ***
# 패턴 발견 여부에 따라 증가시켜야 하는 인덱스 크기가 달라지기 때문 !
while idx < m - 1:
  if s[idx-1] == 'I' and s[idx] == 'O' and s[idx+1] == 'I':
    p_count += 1
    if p_count == n:
      p_count -= 1
      count += 1
    idx += 1 # 패턴이 발견되면 총 두 칸(인덱스)을 증가시켜야 함(1)
  else:
    p_count = 0 # 연속적으로 발견되지 못했으므로 초기화
  
  idx += 1 # 패턴이 발견되면 총 두 칸(인덱스)을 증가시켜야 함(2)

  
# 시간복잡도 : O(M)
print(count)