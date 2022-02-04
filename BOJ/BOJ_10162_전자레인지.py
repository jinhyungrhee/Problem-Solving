t = int(input())

button_list = [300, 60, 10]

for button in button_list:
    if t % 10 != 0:
        print(-1)
        break
    if t >= button:
        print(t // button, end=" ")
        t %= button
    else:
        print(0, end=" ")