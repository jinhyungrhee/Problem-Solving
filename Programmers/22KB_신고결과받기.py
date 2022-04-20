id_list = ["muzi", "frodo", "apeach", "neo"]
report = ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]
k = 2

# id_list = ["con", "ryan"]
# report = ["ryan con", "ryan con", "ryan con", "ryan con"]
# k = 3

def solution(id_list, report, k):
  reportHash = {} # 누가 누구를 신고했는지
  resultHash = {} # 누가 누구로부터 신고당했는지

  for r in report:
    user, bad = r.split()
    if user not in reportHash: # 최초 신고인 경우
      reportHash[user] = set() # set 생성
    reportHash[user].add(bad)

    if bad not in resultHash: # 최초 신고당한 경우
      resultHash[bad] = set() # set 생성
    resultHash[bad].add(user)

    answer = [0 for _ in range(len(id_list))]

    # id_list에 존재하는 user들을 하나씩 확인
    for i in range(len(id_list)):
      user = id_list[i]
      if user not in reportHash: # reportHash에 없으면 user가 신고한 적이 없음
        continue

      for bad in reportHash[user]: # user가 신고한 사람들의 set 탐색
        # 거기에 있는 bad의 resultHash 크기가 K 이상이면 정지
        if len(resultHash[bad]) >= k:
          answer[i] += 1

  return answer

print(solution(id_list, report, k))
