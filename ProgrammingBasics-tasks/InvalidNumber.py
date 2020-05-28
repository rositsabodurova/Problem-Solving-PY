num = int(input())

is_valid = False

if num >= 100 and num <= 200:
    is_valid = True
elif num == 0:
    is_valid = True

if is_valid== False:
    print("invalid")