num_of_iterations = int(input())

p1_count = 0
p2_count = 0
p3_count = 0
p4_count = 0
p5_count = 0

for i in range(0, num_of_iterations):
    current_num = int(input())
    if current_num < 200:
        p1_count += 1
    elif 200 <= current_num <= 399:
        p2_count += 1
    elif 400 <= current_num <= 599:
        p3_count += 1
    elif 600 <= current_num <= 799:
        p4_count += 1
    elif current_num >= 800:
        p5_count += 1

percentage_p1 = p1_count / num_of_iterations * 100
percentage_p2 = p2_count / num_of_iterations * 100
percentage_p3 = p3_count / num_of_iterations * 100
percentage_p4 = p4_count / num_of_iterations * 100
percentage_p5 = p5_count / num_of_iterations * 100

print(f"{percentage_p1:.2f}%")
print(f"{percentage_p2:.2f}%")
print(f"{percentage_p3:.2f}%")
print(f"{percentage_p4:.2f}%")
print(f"{percentage_p5:.2f}%")