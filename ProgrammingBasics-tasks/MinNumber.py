iterations = int(input())
counter = 0

import sys
min_num = sys.maxsize

while counter < iterations:
    current_num = int(input())
    if current_num < min_num:
        min_num = current_num
    counter += 1

print(min_num)