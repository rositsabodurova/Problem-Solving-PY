command = input()

while command.lower() != "end":
    min_budget = float(input())
    sum = 0
    while sum < min_budget:
        sum += float(input())
    print(f"Going to {command}!")
    command = input()