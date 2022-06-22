def solution(participant, completion):
    answer = ''
    hashDict = {}
    sumHash = 0
    for part in participant:
        hashDict[hash(part)] = part # hash()는 각 값에 따른 고유한 hash값을 생성하는 함수
        sumHash += hash(part)
        # print(hash(part), sumHash)
        
    # print()
    for comp in completion:
        sumHash -= hash(comp)
        # print(hash(comp), sumHash)
    
    # print(hashDict)
    # print(hashDict[sumHash])
    answer = hashDict[sumHash]
    
    return answer