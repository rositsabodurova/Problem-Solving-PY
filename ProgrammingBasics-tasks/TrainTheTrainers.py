jury_count = int(input())
presentation_name = input()
sum_grades = 0
grade_count = 0

while presentation_name != "Finish":
    sum_grades_presentation = 0
    for i in range(0, jury_count):
        grade = float(input())
        sum_grades_presentation += grade
        sum_grades += grade
        grade_count += 1
    average_per_presentation = sum_grades_presentation / jury_count
    print(f"{presentation_name} - {average_per_presentation:.2f}.")
    presentation_name = input()

average_grade = sum_grades / grade_count
print(f"Student's final assessment is {average_grade:.2f}.")
