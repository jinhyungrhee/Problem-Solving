# 구현 - 재귀함수 사용

# '균형잡힌 문자열'의 인덱스 반환
def balanced_index(p):
  count = 0
  for i in range(len(p)):
    if p[i] == '(':
      count += 1
    else:
      count -= 1
    if count == 0:
      return i

# '올바른 괄호 문자열'인지 판단
def check_proper(p):
  # 왼쪽 괄호의 개수
  count = 0
  for i in p:
    if i == '(':
      count += 1
    else:
      # 중간에 count가 0이되면 쌍이 맞지 않는 것
      if count == 0:
        return False
      count -=1 
  # 아무 문제 없이 for문이 끝나면 쌍이 맞는 것
  return True

def solution(p):
  answer = '' # 빈 문자열
  if p == '':
    return answer
  index = balanced_index(p)
  # u와 v로 나누기
  u = p[:index + 1]
  v = p[index + 1:]
  
  # u가 '올바른 괄호 문자열'이면, v에 대해 재귀적으로 호출한 결과 붙여서 반환
  if check_proper(u):
    answer = u + solution(v)
  # u가 '올바른 괄호 문자열'이 아니면
  else:
    answer = '('
    answer += solution(v)
    answer += ')'
    # u의 첫번째 문자와 마지막 문자를 제거
    u = list(u[1:-1])
    # 이외의 문자 뒤집기
    for i in range(len(u)):
      if u[i] == '(':
        u[i] = ')'
      else:
        u[i] = '('
    # 뒤집은 문자열 결과에 붙이기
    answer += "".join(u) # 리스트를 string으로 변경
  return answer

p = "(())))(("
print(solution(p))