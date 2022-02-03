'''
#1
정확성: 22.8
효율성: 0.0
합계: 22.8 / 100.0
'''

#food_times = [3, 1, 2]
#k = 5

food_times = list(map(int, input().split()))
k = int(input())

sec = 0
idx = 0

while True:
  if idx == len(food_times):
    idx = 0
  if sec == k:
    break
  if food_times[idx] == 0:
    idx += 1
    continue
  
  food_times[idx] -= 1
  idx += 1
  sec += 1

print(food_times)
print(idx)
print(sec)