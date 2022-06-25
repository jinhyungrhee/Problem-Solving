def solution(number, k):
    answer = ''
    stack = []
    stack.append(number[0])
    
    # 더 큰 숫자가 stack에 들어오면 pop()하고 k를 감소시킴
    for i in range(1, len(number)):
        idx = i
        # while stack 이면 stack이 비었을 때(=초기 stack일 때)는 수행되지 않으므로 0번째 인덱스에서부터 수행해도 상관없음!
        while stack and stack[-1] < number[idx]:
            if k == 0:
                break
            stack.pop()
            k -= 1
        stack.append(number[idx])
    
    answer = ''.join(stack[:len(stack) - k]) # [9, 9, 9], k = 2의 경우, 변화가 없으므로 전체 길이에서 k를 뺀 만큼만 출력
        
    return answer

# 조금 더 단순화한 코드 (0번째 인덱스부터 for문 돌리기 + 'while stack' 사용) ***
'''
def solution(number, k):
  answer = ''
  stack = []
  
  # 더 큰 숫자가 stack에 들어오면 pop()하고 k를 감소시킴
  for num in number:
    while stack and k > 0 and stack[-1] < num:
      stack.pop()
      k -= 1
    stack.append(num)

  answer = ''.join(stack[:len(stack) - k])

  return answer
'''