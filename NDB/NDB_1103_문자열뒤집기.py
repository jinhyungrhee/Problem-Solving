# BOJ_1439_뒤집기 문제

'''
#1 코드 보완 필요 - 두 가지 경우를 모두 고려하기(= min함수 사용!)
'''

data = input()

# 첫번째 문자 추출
first = data[0]
now_bit = data[0]

# 다른 문자로 바뀌는 첫번째 부분만 체크
count = 0
for i in range(1, len(data)):
  if data[i] != first and data[i] != now_bit:
    now_bit = data[i]
    count += 1
  elif data[i] == first and data[i] != now_bit:
    now_bit = data[i]

print(count)

''' 
#2
'''