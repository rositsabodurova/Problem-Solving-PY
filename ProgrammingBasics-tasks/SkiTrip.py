days = int(input())
room_type = input()
assessment = input()

sum = 0

if room_type == "room for one person":
    sum = (days - 1) * 18
elif room_type == "apartment":
    sum = (days - 1) * 25
    if days < 10:
        sum = sum * 0.7
    elif days <= 15:
        sum = sum * 0.65
    elif days > 15:
        sum = sum * 0.5
elif room_type == "president apartment":
    sum = (days - 1) * 35
    if days < 10:
        sum = sum * 0.9
    elif days <= 15:
        sum = sum * 0.85
    elif days > 15:
        sum = sum * 0.8

if assessment == "positive":
    sum = sum * 1.25
else:
    sum = sum * 0.9

print(f"{sum:.2f}")

