trip_price = float(input())
puzzles_count = int(input())
dolls_count = int(input())
bears_count = int(input())
minions_count = int(input())
trucks_count = int(input())

total_count = puzzles_count + dolls_count + bears_count + minions_count + trucks_count
total_money = (puzzles_count * 2.6) + (dolls_count * 3) + (bears_count * 4.1) + (minions_count * 8.2) + (trucks_count * 2)

if total_count >= 50:
    total_money = total_money * 0.75

total_money = total_money * 0.9

if total_money >= trip_price:
    print(f"Yes! {total_money - trip_price:.2f} lv left.")
else:
    print(f"Not enough money! {trip_price - total_money:.2f} lv needed.")