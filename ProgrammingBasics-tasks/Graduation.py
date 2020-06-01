name = input()

grades_sum = 0
classes = 1

while classes <= 12:
    grade = float(input())
    if grade < 4:
        continue
    grades_sum += grade
    classes += 1

average_grade = grades_sum / 12

print(f"{name} graduated. Average grade: {average_grade:.2f}")
