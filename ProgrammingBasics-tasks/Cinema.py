type = input()
rows = int(input())
columns = int(input())

seats_count = rows * columns
income = 0

if type == "Premiere":
    income = seats_count * 12
elif type == "Normal":
    income = seats_count * 7.5
else:
    income = seats_count * 5

print(f"{income:.2f} leva")