import copy
n = int(input())

A = list(map(int, input().split()))
B = list(map(int, input().split()))

tmp = copy.deepcopy(B)
A.sort()
new_A = [0] * n

for i in range(n):
  max_val = 0
  max_idx = 0
  for j in range(n):
    if tmp[j] >= max_val:
      max_val = tmp[j]
      max_idx = j
  # 최대값을 찾았으면 A의 가장 작은값을 해당 인덱스로 이동
  new_A[max_idx] = A[i]
  tmp[max_idx] = -1

# print(new_A)
# print(B)

sum_val = 0
for i in range(n):
  sum_val += new_A[i] * B[i]

print(sum_val)