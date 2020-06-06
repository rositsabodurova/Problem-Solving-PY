num = int(input())

is_special = True

for i in range(1111, 10000):
    current = i
    for j in range(1, 5):
        last_digit = current % 10
        current = current // 10
        if last_digit == 0:
            is_special = False
            break
        if num % last_digit != 0:
            is_special = False
            break
    if is_special:
        print(i, end=" ")
    is_special = True