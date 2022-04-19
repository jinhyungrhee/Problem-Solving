'''
# s = "one4seveneight"
# s = "23four5six7"
s = "2three45sixseven"
# s = "123"

# 영어로 시작하는 경우
# 숫자로 시작하는 경우

num_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
alpha_list = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
three_letter = ['one', 'two', 'six'] # 3
four_letter = ['zero', 'four', 'five', 'nine'] # 4
five_letter = ['three', 'seven', 'eight'] # 5

# 일단 숫자와 문자를 분리하고,
# 결합된 문자들은 3글자, 4글자, 5글자로 체크

def solution(s):
  total = []
  n = len(s)
  start, end = 0, 0
  
  for i in range(1, n):
    if s[i-1].isalpha() and s[i].isnumeric():
      # print('n_idx: ' + s[i]) # n_idx
      end = s.index(s[i])
      total.append(list(s[start:end]))
      start = end
    elif s[i-1].isnumeric() and s[i].isalpha():
      # print('l_idx: ' + s[i]) # l_idx
      end = s.index(s[i])
      total.append(list(s[start:end]))
      start = end
  # 마지막 추가
  total.append(list(s[start:n+1]))
      
  # print(total)

  answer = ''
  
  for elem in total:
    if elem[0].isnumeric(): # 숫자
      for i in elem:
        answer += i
    else: # 문자
      while elem:
        # check three
        for i in range(0, len(elem), 3):
          # print(''.join(tmp[i:i+3]))
          three_word = ''.join(elem[i:i+3])
          if three_word in three_letter:
            # elem.append(three_word)
            answer += str(alpha_list.index(three_word))
            del elem[i:i+3]
            # print(three_word)
  
        # check four
        for i in range(0, len(elem), 4):
          # print(''.join(tmp[i:i+4]))
          four_word = ''.join(elem[i:i+4])
          if four_word in four_letter:
            # elem.append(four_word)
            answer += str(alpha_list.index(four_word))
            del elem[i:i+4]
  
        # check five
        for i in range(0, len(elem), 5):
          # print(''.join(tmp[i:i+5]))
          five_word = ''.join(elem[i:i+5])
          if five_word in five_letter:
            # elem.append(five_word)
            answer += str(alpha_list.index(five_word))
            del elem[i:i+5]
        

  # print(total)
  # print(answer)
  return int(answer)
      
solution(s)
'''

# 모범 답안

s = "one4seveneight"
# s = "23four5six7"
# s = "2three45sixseven"
# s = "123"

def solution(s):
  while s.isdigit() == False: # s에 영단어가 존재하는 동안 반복
    if s.find('one') != -1: # 'one'이 존재하면
      s = s.replace('one', '1')
    elif s.find('two') != -1:
      s = s.replace('two', '2')
    elif s.find('three') != -1:
      s = s.replace('three', '3')
    elif s.find('four') != -1:
      s = s.replace('four', '4')
    elif s.find('five') != -1:
      s = s.replace('five', '5')
    elif s.find('six') != -1:
      s = s.replace('six', '2')
    elif s.find('seven') != -1:
      s = s.replace('seven', '7')
    elif s.find('eight') != -1:
      s = s.replace('eight', '8')
    elif s.find('nine') != -1:
      s = s.replace('nine', '9')
    elif s.find('zero') != -1:
      s = s.replace('zero', '0')
    else:
      None
  return int(s)

print(solution(s))