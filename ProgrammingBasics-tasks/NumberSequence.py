num_iterations = int(input())

import sys
min_num = sys.maxsize
max_num = -sys.maxsize

for num in range(0, num_iterations):
    current_num = int(input())
    if current_num > max_num:
        max_num = current_num
    if current_num < min_num:
        min_num = current_num

print(f"Max number: {max_num}")
print(f"Min number: {min_num}")