def solution(record):
    answer = []
    result = []
    hash_map = {}
    
    for r in record:
        order = r.split(" ")[0]
        uid = r.split(" ")[1]
        if order == "Leave":
            answer.append(uid + "님이 나갔습니다.")
        else:    
            nickname = r.split(" ")[2]
            hash_map[uid] = nickname
            if order == "Enter":
                answer.append(uid + "님이 들어왔습니다.")
    
    # print(hash_map)
    # print(answer)
    
    for a in answer:
        target = a.split("님")[0]
        result.append(a.replace(target, hash_map[target]))
        
    return result