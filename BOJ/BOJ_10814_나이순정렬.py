n = int(input())

accounts = []

for i in range(n): 
  data = input().split()
  accounts.append([i, int(data[0]), data[1]])

accounts.sort(key=lambda x:(x[1], x[0]))

for account in accounts:
  print(account[1], account[2])