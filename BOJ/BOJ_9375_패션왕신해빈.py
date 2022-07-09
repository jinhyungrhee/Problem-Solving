tc = int(input())

for _ in range(tc):
  n = int(input())
  fashion = {}
  for _ in range(n):
    name, category = input().split()
    if category not in fashion:
      fashion[category] = 1
    else:
      fashion[category] = fashion.get(category) + 1

  # print(fashion)
  result = 1
  for k, v in fashion.items():
    result *= (v + 1)

  print(result - 1)