n = 1260 # 받은 돈
count = 0

coin_types = [500, 100, 50, 10] # 동전 종류

for coin in coin_types:
    count += n // coin
    n %= coin

print(count)
