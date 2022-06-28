# 220628

s = 'abcabcabcabcdededededede'

answer = len(s) # 처음 문자열 길이

for step in range(1, len(s)//2 + 1):
  compressed = ''
  prev = s[0:step] # 이전 문자열
  # print(prev)
  count = 1
  for j in range(step, len(s), step):
    if prev == s[j:j+step]: # s[j:j+step] - 현재 문자열
      count += 1
    else: # 이전 문자열과 현재 문자열이 다르면
      # 지금까지 압축한 내용 저장
      compressed += str(count) + prev if count >= 2 else prev
      prev = s[j:j+step] # 현재 문자열을 이전 문자열로 변경
      count = 1

  # j-for문이 종료된 후에 마지막 압축 내용이 반영되지 않을 수 있음
  compressed += str(count) + prev if count >= 2 else prev

  answer = min(answer, len(compressed))
  print(compressed)

print(answer)

'''
def solution(word):
  n = len(word)
  # step 1부터 비교
  for step in range(1, n//2+1):
    compressed = ""
    prev = word[0:step]
    cnt = 1
    # 단위 크기만큼 증가시키면서 비교
    for j in range(step, n, step):
      if prev == word[j:j+step]:
        cnt += 1
      else:
        compressed += str(cnt) + prev if cnt >= 2 else prev
        # 초기화
        prev = word[j:j+step]
        cnt = 1
    # 남아 있는 문자열에 대해서 처리 (?)
    compressed += str(cnt) + prev if cnt >= 2 else prev
    # 가장 짧은 문자열 출력
    print(compressed)
    n = min(n, len(compressed))
  
  return n

word = "aaaabbabbabb"
print(solution(word))
'''