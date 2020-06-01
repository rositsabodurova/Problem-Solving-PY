iterations = int(input())

counter = 0
balance = 0

while counter < iterations:
    sum = float(input())
    if sum >= 0:
        balance += sum
        print(f"Increase: {sum:.2f}")
    else:
        print("Invalid operation!")
        break
    counter += 1

print(f"Total: {balance:.2f}")
