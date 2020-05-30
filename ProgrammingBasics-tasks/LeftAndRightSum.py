num_of_iterations = int(input())

left_sum = 0
right_sum = 0

for i in range(1, num_of_iterations + 1):
    current_num = int(input())
    left_sum += current_num
for i in range(num_of_iterations * 2, num_of_iterations, -1):
    current_num = int(input())
    right_sum += current_num

if left_sum == right_sum:
    print(f"Yes, sum = {right_sum}")
else:
    difference = abs(right_sum - left_sum)
    print(f"No, diff = {difference}")
