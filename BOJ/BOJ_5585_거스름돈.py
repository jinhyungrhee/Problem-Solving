change = 1000 - int(input())

coin_list = [500, 100, 50, 10, 5, 1]

cnt = 0

for coin in coin_list:
    if change >= coin:
        cnt += change // coin
        change %= coin
        
print(cnt)