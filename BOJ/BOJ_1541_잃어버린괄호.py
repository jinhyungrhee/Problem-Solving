data = input().split('-')

def get_sum(str):
  tmp = list(map(int, str.split('+')))
  sum_val = sum(tmp)
  return sum_val
    
for i in range(len(data)):
  if not data[i].isdigit():
    tmp = get_sum(data[i])
    data[i] = tmp

result = int(data[0])
for i in range(1, len(data)):
  result -= int(data[i])

print(result)