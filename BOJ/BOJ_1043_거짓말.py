import sys
input = sys.stdin.readline
n, m = map(int, input().split())

p_parent = [i for i in range(n+1)]

def union_parent(parent, a, b):
  a = find_parent(parent, a)
  b = find_parent(parent, b)
  if a < b:
    parent[b] = a
  else:
    parent[a] = b
  
def find_parent(parent, x):
  if parent[x] != x: # 경로 단축
    parent[x] = find_parent(parent, parent[x])
  return parent[x]

knowing = list(map(int, input().split()))
n_knowing = knowing[0]
p_knowing = knowing[1:]

party = []
count = 0
for _ in range(m):
  data = list(map(int, input().split()))
  n_people = data[0]
  p_people = data[1:]
  for i in range(n_people-1):
    union_parent(p_parent, p_people[i], p_people[i+1])
  party.append(p_people)
 
# print(party)
# print(p_parent)
# print(p_knowing)

# p_parent 리스트에 대해 경로단축 한번더 수행
# -> 최종적으로 확정된 포함관계 계산하기 위해!
for i in range(1, len(p_parent)):
  if p_parent[i] != i:
    p_parent[i] = find_parent(p_parent, p_parent[i])
  
for i in range(len(party)):
  is_checked = False
  for j in range(len(party[i])):
    for k in range(len(p_knowing)):
      if p_parent[party[i][j]] == p_parent[p_knowing[k]]:
        is_checked = True
  if is_checked:
    count += 1

print(m - count)

# 반례 : https://www.acmicpc.net/board/view/85017