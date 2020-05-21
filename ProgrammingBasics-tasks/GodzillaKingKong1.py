available_budget = float(input())
actors_count = int(input())
costume_price = float(input())

decor_price = available_budget * 0.1

costume_money = costume_price * actors_count
if actors_count > 150:
    costume_money = costume_money * 0.9

total_money = costume_money + decor_price
difference = abs(total_money - available_budget)

if total_money > available_budget:
    print("Not enough money!")
    print(f"Wingard needs {difference:.2f} leva more.")
else:
    print("Action!")
    print(f"Wingard starts filming with {difference:.2f} leva left.")