num_of_iterations = int(input())

even_sum = 0
odd_sum = 0

for i in range(1, num_of_iterations + 1):
    current_num = int(input())
    if i % 2 == 0:
        even_sum += current_num
    else:
        odd_sum += current_num

if even_sum == odd_sum:
    print("Yes")
    print(f"Sum = {odd_sum}")
else:
    difference = abs(odd_sum - even_sum)
    print("No")
    print(f"Diff = {difference}")