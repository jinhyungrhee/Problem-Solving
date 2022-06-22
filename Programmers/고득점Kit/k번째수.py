def solution(array, commands):
    answer = []
    
    for command in commands:
        i = command[0] - 1
        j = command[1]
        k = command[2] - 1
        # print(array[i:j])
        new_array = sorted(array[i:j])
        # print(new_array[k])
        answer.append(new_array[k])

    return answer