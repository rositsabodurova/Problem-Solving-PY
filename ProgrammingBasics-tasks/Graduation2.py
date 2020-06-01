name = input()

sum_grades = 0
classes = 1
exclusion_criteria = 0

while classes <= 12:
    current_grade = float(input())
    if current_grade < 4:
        exclusion_criteria += 1
        if exclusion_criteria == 2:
            break
        continue

    sum_grades += current_grade
    classes += 1

if exclusion_criteria == 2:
    print(f"{name} has been excluded at {classes} grade")
else:
    average_grade = sum_grades / 12
    print(f"{name} graduated. Average grade: {average_grade:.2f}")