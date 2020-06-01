cake_width = int(input())
cake_length = int(input())

cake_size = cake_length * cake_width
command = input()
is_over = False

while command != "STOP":
    pieces = int(command)
    cake_size -= pieces
    if cake_size <= 0:
        is_over = True
        break
    command = input()
if is_over:
    print(f"No more cake left! You need {abs(cake_size)} pieces more.")
else:
    print(f"{cake_size} pieces are left.")