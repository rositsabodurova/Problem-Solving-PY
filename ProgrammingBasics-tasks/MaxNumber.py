iterations = int(input())
counter = 0

import sys
max_num = -sys.maxsize

while counter < iterations:
    current_num = int(input())
    if current_num > max_num:
        max_num = current_num
    counter += 1

print(max_num)