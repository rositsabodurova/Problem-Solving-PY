flower_type = input()
flower_count = int(input())
budget = int(input())

total_money = 0

if flower_type == "Roses":
    total_money = flower_count * 5
    if flower_count > 80:
        total_money = total_money * 0.9
elif flower_type == "Dahlias":
    total_money = flower_count * 3.8
    if flower_count > 90:
        total_money = total_money * 0.85
elif flower_type == "Tulips":
    total_money = flower_count * 2.8
    if flower_count > 80:
        total_money = total_money * 0.85
elif flower_type == "Narcissus":
    total_money = flower_count * 3
    if flower_count < 120:
        total_money = total_money * 1.15
elif flower_type == "Gladiolus":
    total_money = flower_count * 2.5
    if flower_count < 80:
        total_money = total_money * 1.2

difference = abs(budget - total_money)

if budget >= total_money:
    print(f"Hey, you have a great garden with {flower_count} {flower_type} and {difference:.2f} leva left.")
else:
    print(f"Not enough money, you need {difference:.2f} leva more.")