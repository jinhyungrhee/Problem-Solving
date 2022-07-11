import sys

tc = int(sys.stdin.readline())

for _ in range(tc):
  sys.stdin.readline()
  n, m = map(int, sys.stdin.readline().split())
  A = list(map(int, sys.stdin.readline().split()))
  B = list(map(int, sys.stdin.readline().split()))

  sum_A = sum(A)
  avg_A = sum_A/n
  sum_B = sum(B)
  avg_B = sum_B/m

  count = 0
  for i in range(n):
    if A[i] < avg_A and A[i] > avg_B:
      count += 1

  print(count)