def solution(N, stages):
    fail = [] 
    answer = []
    user_num = len(stages)
    stages.sort()
    
    for j in range(N):
        cnt = 0
        for elem in stages:
            if elem == j + 1:
                cnt += 1
        if user_num == 0:
            fail.append((0, j + 1))
        else:
            fail.append((cnt / user_num, j + 1))
        user_num -= cnt
    
    fail.sort(key=lambda x : -x[0])
    
    for i in range(N):
        answer.append(fail[i][1])
        
    return answer

'''답안(조금 더 가독성이 높은 코드)
def solution(N, stages):
  answer = []
  length = len(stages)

  for i in range(1, N + 1):
    count = stages.count(i)

    if length == 0:
      fail = 0
    else:
      fail = count / length

    answer.append((i, fail))
    length -= count

  answer = sorted(answer, key=lambda x:x[1], reverse=True)

  # 첫번째 원소만 뽑아서 answer 리스트 재구성
  answer =[i[0] for i in answer]
  return answer
'''