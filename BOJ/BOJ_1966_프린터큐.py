tc = int(input())
for _ in range(tc):
  queue = []
  n, m = map(int, input().split())
  tmp = list(map(int, input().split()))
  for i in range(len(tmp)):
    queue.append((tmp[i], i))
    
  # print()
  # print(queue)
  # print()

  count = 0
  while queue:
    curr = queue.pop(0)
    if queue and curr[0] < max(queue)[0]: # 우선순위 비교
      queue.append(curr) # 큐의 최대값(max(queue))보다 작은 것들은 모두 뒤로 보냄
    else:
      count += 1
      if curr[1] == m:
        print(count)