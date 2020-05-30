num_of_iterations = int(input())

p1_counter = 0
p2_counter = 0
p3_counter = 0

for i in range(0, num_of_iterations):
    current_num = int(input())
    if current_num % 2 == 0:
        p1_counter += 1
    if current_num % 3 == 0:
        p2_counter += 1
    if current_num % 4 == 0:
        p3_counter += 1

percentage_p1 = p1_counter / num_of_iterations * 100
percentage_p2 = p2_counter / num_of_iterations * 100
percentage_p3 = p3_counter / num_of_iterations * 100

print(f"{percentage_p1:.2f}%")
print(f"{percentage_p2:.2f}%")
print(f"{percentage_p3:.2f}%")