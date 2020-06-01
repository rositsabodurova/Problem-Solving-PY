change = float(input())
coin_count = 0

import math

change = math.floor(change * 100)

while change > 0:
    if change >= 200:
        coin_count += 1
        change -= 200
    elif change >= 100:
        coin_count += 1
        change -= 100
    elif change >= 50:
        coin_count += 1
        change -= 50
    elif change >= 20:
        coin_count += 1
        change -= 20
    elif change >= 10:
        coin_count += 1
        change -= 10
    elif change >= 5:
        coin_count += 1
        change -= 5
    elif change >= 2:
        coin_count += 1
        change -= 2
    elif change >= 1:
        coin_count += 1
        change -= 1

print(coin_count)
