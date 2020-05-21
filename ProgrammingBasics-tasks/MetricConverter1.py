number = float(input())
first_metric = input()
second_metric = input()

result = 0;

if first_metric == "m":
    if second_metric == "cm":
        result = number * 100
    elif second_metric == "mm":
        result = number * 1000
elif first_metric == "cm":
    if second_metric == "mm":
        result = number * 10
    elif second_metric == "m":
        result = number / 100
else:
    if second_metric == "cm":
        result = number / 10
    elif second_metric == "m":
        result = number /1000

print(f"{result:.3f}")