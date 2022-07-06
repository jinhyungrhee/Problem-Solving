import math

A, B, V = map(int, input().split())

ordinary = A - B # 일반적인 하루동안 올라가는 높이
last = A # 마지막 반나절에 올라가는 높이

days = V - last # 전체 길이에서 마지막 반나절에 올라갈 수 있는 높이를 뺀 길이

print(math.ceil(days / ordinary) + 1) # 일반적으로 올라가는 날 수를 구하고 거기에 마지막 반나절(하루)을 더함

