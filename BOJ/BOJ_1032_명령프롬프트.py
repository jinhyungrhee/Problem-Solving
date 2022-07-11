n = int(input())

result = ''
tmp = ''
result = list(input())
for _ in range(n-1):
  tmp = list(input())
  for i in range(len(result)):
    if result[i] != tmp[i]:
      # result = result.replace(result[i], "?", 1)
      result[i] = '?'

result = ''.join(result)
print(result)

# ** replace()를 사용하지 못하는 이유 **
# result[i]에 해당하는 문자가 여러 개일 때, 3번째 parameter에 숫자를 지정하지 않으면 모든 문자를 다 "?"로 바꿔버리고
# 이를 방지하기 위해 3번째 parameter에 1(=변경 횟수)을 지정하면, 맨 앞부터 등장하는 숫자를 지정 개수만큼 "?"로 변경함

# 반례
# (입력)
# 2
# abc.....
# abcd.sys
# (결과)
# abc????.
