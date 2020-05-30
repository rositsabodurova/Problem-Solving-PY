num_iterations = int(input())
sum = 0

import sys

max_num = -sys.maxsize

for i in range(1, num_iterations + 1):
    current_num = int(input())
    sum += current_num
    if current_num > max_num:
        max_num = current_num
sum -= max_num

if sum == max_num:
    print("Yes")
    print(f"Sum = {sum}")
else:
    difference = abs(sum - max_num)
    print("No")
    print(f"Diff = {difference}")
