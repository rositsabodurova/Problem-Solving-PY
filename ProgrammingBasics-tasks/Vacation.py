money_needed = float(input())
current_money = float(input())

days_count = 0
spend_days_count = 0
cannot_save = False

while not cannot_save:
    command = input()
    sum = float(input())
    days_count += 1
    if command == "save":
        current_money += sum
        spend_days_count = 0
        if current_money >= money_needed:
            break
    else:
        if sum > current_money:
            current_money = 0
        else:
            current_money -= sum
            spend_days_count += 1
            if spend_days_count == 5:
                cannot_save = True
                break

if cannot_save:
    print("You can't save the money.")
    print(days_count)
else:
    print(f"You saved the money for {days_count} days.")