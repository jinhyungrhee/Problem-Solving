def solution(numbers, hand):
    answer = ''
    key = {
        '1': {'2': 1, '5': 2, '8': 3, '0': 4},
        '2': {'2': 0, '5': 1, '8': 2, '0': 3},
        '3': {'2': 1, '5': 2, '8': 3, '0': 4},
        '4': {'2': 2, '5': 1, '8': 2, '0': 3},
        '5': {'2': 1, '5': 0, '8': 1, '0': 2},
        '6': {'2': 2, '5': 1, '8': 2, '0': 3},
        '7': {'2': 3, '5': 2, '8': 1, '0': 2},
        '8': {'2': 2, '5': 1, '8': 0, '0': 1},
        '9': {'2': 3, '5': 2, '8': 1, '0': 2},
        '0': {'2': 3, '5': 2, '8': 1, '0': 0},
        '*': {'2': 4, '5': 3, '8': 2, '0': 1},
        '#': {'2': 4, '5': 3, '8': 2, '0': 1}
     }
    
    lprev = '*'
    rprev = '#'
    for num in numbers:
        num = str(num)
        if num == '1' or num == '4' or num == '7':
            answer += 'L'
            lprev = num
        elif num == '3' or num == '6' or num == '9':
            answer += 'R'
            rprev = num
        else:
            if key[lprev][num] < key[rprev][num]:
                answer += 'L'
                lprev = num
            elif key[lprev][num] > key[rprev][num]:
                answer += 'R'
                rprev = num
            else:
                if hand == 'left':
                    answer += 'L'
                    lprev = num
                else:
                    answer += 'R'
                    rprev = num
                    
    return answer

print(solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 0], "right"))