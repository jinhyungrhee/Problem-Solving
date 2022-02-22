# '튜플을 원소로 하는 리스트'를 정렬하면 기본적으로 각 튜플을 구서하는 원소의 순서에 맞게 정렬됨
# 리스트의 원소를 정렬할 때는 sort()함수의 key 속성에 값을 대입하여 내가 원하는 '조건'에 맞게 튜플을 정렬시킬 수 있음

n = int(input())
students = []

# 모든 학생 정보 입력받음
for _ in range(n):
    students.append(input().split()) 

# 조건을 차례 대로 '튜플'형식으로 작성
students.sort(key=lambda x: (-int(x[1]), int(x[2]), -int(x[3]), x[0]))

# 이름 출력
for student in students:
    print(student[0])

'''
n = int(input())

student = []

for _ in range(n):
  name, s1, s2, s3 = map(str, input().split())
  s1, s2, s3 = int(s1), int(s2), int(s3)
  student.append((name, s1, s2, s3))

#print(student)
# 조건을 차례 대로 '튜플' 형식으로 작성
student.sort(key=lambda x: (-x[1], x[2], -x[3], x[0]))

for i in range(n):
  print(student[i][0])
'''