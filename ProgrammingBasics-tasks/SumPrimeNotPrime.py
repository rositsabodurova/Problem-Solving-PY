command = input()

prime_sum = 0
not_prime_sum = 0
is_negative = False

while command != "stop":
    is_not_prime = False
    current_num = int(command)
    if current_num < 0:
        is_negative = True
    if not is_negative:
        for i in range(2, current_num):
            if current_num % i == 0:
                is_not_prime = True
                break
        if is_not_prime:
            not_prime_sum += current_num
        else:
            prime_sum += current_num
        command = input()
    else:
        print("Number is negative.")
        is_negative = False
        command = input()

print(f"Sum of all prime numbers is: {prime_sum}")
print(f"Sum of all non prime numbers is: {not_prime_sum}")
