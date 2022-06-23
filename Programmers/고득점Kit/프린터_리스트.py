def solution(priorities, location):
    answer = 0
    
    array1 = [idx for idx in range(len(priorities))] # 인덱스(위치) 리스트
    array2 = priorities.copy() # 값 리스트
    
    i = 0
    while True:
        # <queue 원리를 이용하여 내림차순으로 정렬>***
        # 인덱스(i)를 증가시키면서 arr2 리스트의 맨 앞을 고정시키고 리스트의 나머지 부분을 정렬시킴
        
        # 이후에 큰 값이 존재하면, 해당 값을 맨 뒤로 보냄
        if array2[i] < max(array2[i+1:]):
            array1.append(array1.pop(i))
            array2.append(array2.pop(i))
        # 이후에 큰 값이 존재하지 않으면, 인덱스를 증가시켜 다음 자리수 확인(앞자리는 고정됨)***
        else:
            i += 1
            
        # 종료조건 -> array2가 내림차순으로 정렬되었을 때 종료 
        if array2 == sorted(array2, reverse=True):
            break
            
    # 값 리스트가 내림차순으로 정렬되었을 때, 인덱스(위치) 리스트에서 최종 순서(+1)를 구해서 리턴
    return array1.index(location) + 1


print(solution([1, 2, 3, 2], 2))