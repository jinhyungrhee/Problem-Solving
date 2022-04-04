n = int(input())

examinees = list(map(int, input().split()))

main, sub = tuple(map(int, input().split()))

result = 0

for examinee in examinees:
  examinee -= main # 감독관 반드시 한명 참여
  result += 1

  # 나머지 학생들 가지고
  if examinee > 0:
    result += examinee // sub # 부 감독관 수 계산

    if examinee % sub > 0: # 만약 나눴을 때 나머지가 존재하면
      result += 1 # 1 더 증가시킴

print(result)


''' 오답
n = int(input())

examinees = list(map(int, input().split()))

main, sub = tuple(map(int, input().split()))

main_cnt = 0
for i in range(n):
  if examinees[i] != 0: # 학생 수가 0이 아닌 경우만 계산
    if examinees[i] <= main:
      examinees[i] = 0
    else:
      examinees[i] -= main
    main_cnt += 1

sub_cnt = 0
for i in range(n):
  if examinees[i] != 0: # 남은 학생 수가 0이 아닌 경우만 계산
    if examinees[i] < sub:
      sub_cnt += 1
    elif examinees[i] == sub:
      sub_cnt += (examinees[i] // sub)
    else:
      sub_cnt += (examinees[i] // sub) + 1

print(main_cnt + sub_cnt)
'''