start = int(input())
end = int(input())
magic_number = int(input())

counter = 0
first_num = 0
second_num = 0
is_found = False

for i in range(start, end + 1):
    for j in range(start, end + 1):
        counter += 1
        if i + j == magic_number:
            first_num = i
            second_num = j
            is_found = True
            break
    if is_found:
        break

if is_found:
    print(f"Combination N:{counter} ({first_num} + {second_num} = {magic_number})")
else:
    print(f"{counter} combinations - neither equals {magic_number}")