# HINT : while문이 중간에 끊기면 안 되고, 마지막에 교차되었을 때의 index를 구해야 함

n, m = map(int, input().split())

data = list(map(int, input().split()))

start = 0
end = max(data)
result = 0

while start <= end:
    mid = (start + end) // 2

    remainder = 0
    for elem in data:
        if elem - mid > 0:
            remainder += (elem - mid)

    if remainder < m:
        # start = mid + 1
        end = mid - 1  # remainder 늘리기
    else:
        result = mid
        # end = mid - 1
        start = mid + 1  # remainder 줄이기

print(result)
