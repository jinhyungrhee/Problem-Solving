import sys

k, n = map(int, sys.stdin.readline().split())

array = []

for i in range(k):
    array.append(int(sys.stdin.readline()))

# print(array)

start = 0
end = max(array)
res = 0

while start <= end:

    mid = (start + end) // 2

    sum_val = 0
    for elem in array:
        if elem >= mid:
            sum_val += elem // mid if mid != 0 else elem - mid # ZeroDivisionError 방지

    if sum_val >= n: # 오른쪽 탐색(= 랜선 늘이기)
        result = mid
        start = mid + 1    
    else: # 왼쪽 탐색(= 랜선 줄이기)
        end = mid - 1

print(result)    