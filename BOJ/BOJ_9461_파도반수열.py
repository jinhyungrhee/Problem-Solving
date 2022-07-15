seq = [0] * 100

seq[0] = 1
seq[1] = 1
seq[2] = 1

for i in range(3, 100):
  seq[i] = seq[i-3] + seq[i-2]

tc = int(input())

for _ in range(tc):
  print(seq[int(input())-1])