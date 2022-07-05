from collections import defaultdict

data =  input()
data = data.upper()
hash_map = defaultdict(int)

for d in data:
  hash_map[d] += 1

result = sorted(hash_map.items(), key=lambda x:x[1], reverse=True)

if len(result) == 1:
  print(result[0][0])
else:
  if result[0][1] == result[1][1]:
    print('?')
  else:
    print(result[0][0])