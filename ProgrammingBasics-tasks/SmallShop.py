product = input()
city = input()
quantity = float(input())

sum = 0

if city == "Sofia":
    if product == "coffee":
        sum = quantity * 0.5
    elif product == "water":
        sum = quantity * 0.8
    elif product == "beer":
        sum = quantity * 1.2
    elif product == "sweets":
        sum = quantity * 1.45
    elif product == "peanuts":
        sum = quantity * 1.6
elif city == "Plovdiv":
    if product == "coffee":
        sum = quantity * 0.4
    elif product == "water":
        sum = quantity * 0.7
    elif product == "beer":
        sum = quantity * 1.15
    elif product == "sweets":
        sum = quantity * 1.30
    elif product == "peanuts":
        sum = quantity * 1.5
else:
    if product == "coffee":
        sum = quantity * 0.45
    elif product == "water":
        sum = quantity * 0.7
    elif product == "beer":
        sum = quantity * 1.1
    elif product == "sweets":
        sum = quantity * 1.35
    elif product == "peanuts":
        sum = quantity * 1.55

print(sum)