n = int(input())
bits = [0] * 32
n_b = bin(n)[2:].zfill(32)
# print(n_b)

for i in range(len(n_b)):
  if n_b[i] == '0':
    bits[i] = 1
  else:
    bits[i] = 0

# print(bits)
count = 1
idx = 31
while True:

  if bits[idx] == 0:
    break

  count += 1
  idx -= 1

print(32 - count)

# IDEA : 
# 1. 이진수를 뒤집은 수를 배열로 저장
# 2. 배열 뒤에서부터 연속된 1의 개수 count
# (=> 1을 더하면 연속된 1의 개수만큼 bit가 변경되고 결국 해당 자리수만큼 기존의 이진수와 bit가 동일해짐)
# 3. 전체 bit수(32)에서 count bit 수를 뺌 == 서로 다른 bit의 수