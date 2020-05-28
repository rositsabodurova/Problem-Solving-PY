fruit = input()
day_of_week = input()
quantity = float(input())

sum = 0
to_print_sum = True

if day_of_week in ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday"):
    if fruit == "banana":
        sum = quantity * 2.5
    elif fruit == "apple":
        sum = quantity * 1.2
    elif fruit == "orange":
        sum = quantity * 0.85
    elif fruit == "grapefruit":
        sum = quantity * 1.45
    elif fruit == "kiwi":
        sum = quantity * 2.7
    elif fruit == "pineapple":
        sum = quantity * 5.5
    elif fruit == "grapes":
        sum = quantity * 3.85
    else:
        print("error")
        to_print_sum = False
    if to_print_sum:
        print(f"{sum:.2f}")


elif day_of_week in ("Saturday", "Sunday"):
    if fruit == "banana":
        sum = quantity * 2.7
    elif fruit == "apple":
        sum = quantity * 1.25
    elif fruit == "orange":
        sum = quantity * 0.9
    elif fruit == "grapefruit":
        sum = quantity * 1.60
    elif fruit == "kiwi":
        sum = quantity * 3
    elif fruit == "pineapple":
        sum = quantity * 5.6
    elif fruit == "grapes":
        sum = quantity * 4.2
    else:
        print("error")
        to_print_sum = False
    if to_print_sum:
        print(f"{sum:.2f}")
else:
    print("error")