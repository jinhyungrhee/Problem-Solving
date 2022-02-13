n = int(input())

cnt = 0
for i in range(n):
  word = input()
  flag = True
  for i in range(len(word)):
    for j in range(i+1, len(word)):
      if word[j] != word[i+1] and word[i] == word[j]:
        flag = False
  if flag == True:
    cnt += 1

print(cnt)
