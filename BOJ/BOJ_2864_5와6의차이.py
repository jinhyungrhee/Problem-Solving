a, b = map(str, input().split())

res = []
if '5' in a or '5' in b:
  res.append(int(a.replace('5', '6')) + int(b.replace('5', '6')))
if '6' in a or '6' in b:
  res.append(int(a.replace('6', '5')) + int(b.replace('6', '5')))
if not '6' in a or not '6' in b:
  res.append(int(a) + int(b))

print(min(res), max(res))