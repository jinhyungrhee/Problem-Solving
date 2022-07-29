bj1, bm1 = map(int, input().split())
bj2, bm2 = map(int, input().split())


def gcd(a, b):

    if b == 0:
        return a

    return gcd(b, a % b)


c_bm = bm1 * bm2
n_bj = bj1 * bm2 + bj2 * bm1

gcd_num = gcd(c_bm, n_bj)
if gcd_num == 1:
    print(n_bj, c_bm)
else:
    print(n_bj // gcd_num, c_bm // gcd_num)