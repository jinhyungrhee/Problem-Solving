n = int(input())
has_num = list(map(int, input().split()))

has_num.sort()

m = int(input())
target_num = list(map(int, input().split()))

for elem in target_num:
    flag = False
    s = 0
    e = len(has_num) - 1
    while s <= e:
        m = (s + e) // 2
        if has_num[m] > elem:
            e = m - 1
        elif has_num[m] < elem:
            s = m + 1
        else:
            flag = True
            print(1, end=" ")
            break
    if not flag:
        print(0, end=" ")