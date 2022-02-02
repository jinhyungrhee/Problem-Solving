''' 
#1 조금 더 간단하고 가독성 있게 코드 작성 가능!
'''

n = input()
num_list = list(map(int, str(n)))
#print(num_list)

result = num_list[0]
for i in range(1, len(num_list)):
  if num_list[i] == 0 or num_list[i] == 1 or num_list[i-1] == 0 or num_list[i-1] == 1:
    result += num_list[i]
  else:
    result *= num_list[i]

print(result)

''' 
#2
'''
