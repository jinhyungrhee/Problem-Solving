import sys

m = int(sys.stdin.readline())

data = [i for i in range(1, 21)]

S = set()

for _ in range(m):
  order = sys.stdin.readline().split()
  if order[0] == "add":
    S |= set([int(order[1])])
  elif order[0] == "remove":
    S -= set([int(order[1])])
  elif order[0] == "check":
    if len(S & set([int(order[1])])) > 0:
      print(1)
    else:
      print(0)
  elif order[0] == "toggle":
    if len(S & set([int(order[1])])) > 0:
      S -= set([int(order[1])])
    else:
      S |= set([int(order[1])])
  elif order[0] == "all":
    S = set(data)
  elif order[0] == "empty":
    S = set([])