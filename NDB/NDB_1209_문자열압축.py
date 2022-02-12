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
