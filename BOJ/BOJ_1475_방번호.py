num = list(input())

cnt = [0] * 10

six_check = False
nine_check = False

for n in num:

  # 6이 두번 연속 나올 경우 체크 스킵
  if n == '6':
    if six_check == False:
      cnt[int(n)] += 1
      six_check = True
    else:
      cnt[9] += 1 # 6 대신 9를 쓰는 것이므로 9 count 증가
      six_check = False
    continue
      
  # 9가 두번 연속 나올 경우 체크 스킵
  if n == '9':
    if nine_check == False:
      cnt[int(n)] += 1
      nine_check = True
    else:
      cnt[6] += 1 # 9 대신 6을 쓰는 것이므로 6 count 증가
      nine_check = False
    continue
  
  cnt[int(n)] += 1

# print(cnt)

print(max(cnt))

# 다른 풀이도 구현해보면 좋을 듯!