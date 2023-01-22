tc = int(input())
for _ in range(tc):
    data = list(map(int, input().split()))

    n = data[0]
    avg = sum(data[1:]) // n

    count = 0
    for i in range(1, n + 1):
        if data[i] > avg:
            count += 1

    print("{:.3f}%".format((count / n) * 100))