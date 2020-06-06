num = int(input())
current = 1
is_current_bugger = False

for i in range(1, num + 1):
    for j in range(1, i + 1):
        if current > num:
            is_current_bugger = True
            break
        print(current, end=" ")
        current += 1
    if is_current_bugger:
        break
    print()