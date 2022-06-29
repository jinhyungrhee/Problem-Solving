# 방법1
def rotated(a):
    n = len(a)
    m = len(a[0])

    result = [[0]* n for _ in range(m)]

    for i in range(n):
        for j in range(m):
            result[j][n-i-1] = a[i][j]

    return result

# 방법2
def rotated_v2(array_2d):
    list_of_tuples = zip(*array_2d[::-1])
    return [list(elem) for elem in list_of_tuples]

arr = [[1,2,3],[4,5,6],[7,8,9]]
nm_arr = [[1,2],[3,4],[5,6]]

# 결과
print(rotated(arr)) # [[7,4,1], [8,5,2], [9,6,3]]
print(rotated(nm_arr)) # [[5,3,1], [6,4,2]]

print(rotated_v2(arr)) # [[7,4,1], [8,5,2], [9,6,3]]
print(rotated_v2(nm_arr)) # [[5,3,1], [6,4,2]]