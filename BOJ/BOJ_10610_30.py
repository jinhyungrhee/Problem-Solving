n = list(input())

n.sort(reverse=True)

res = ''
for elem in n:
    res += elem

int_res = int(res)

if int_res % 30 == 0:
    print(int_res)
else:
    print(-1)