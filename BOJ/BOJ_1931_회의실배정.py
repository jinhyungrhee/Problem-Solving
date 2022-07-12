import sys

n = int(sys.stdin.readline())

classes = []

for _ in range(n):
  s, e = map(int, sys.stdin.readline().split())
  classes.append((s, e))

classes.sort(key=lambda x:(x[1], x[0]))

count = 0
end = 0
for i in range(len(classes)):
  if end <= classes[i][0]:
    end = classes[i][1]
    count += 1

print(count)

# ** 반례 **
# 2 
# 1 1
# 0 1 
# 시작하자마자 끝나는 회의가 있을 수 있음!
# 이 경우, 만약 끝나는 시간이 같다면 먼저 시작하는 회의가 앞에 오도록 정렬 기준을 설정해야 함!