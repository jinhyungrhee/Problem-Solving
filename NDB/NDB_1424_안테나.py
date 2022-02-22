# 중간값(median) 찾기

n = int(input())
houses = list(map(int, input().split()))

# 오름차순 정렬
houses.sort()

# 중간값(median) 출력
print(houses[(n- 1) // 2])


'''
중간값에서 벗어날수록 모든 집까지의 거리의 총합은 증가하게 됨
'''