poor_grades_allowed = int(input())
command = input()
task_count = 0
grades_sum = 0
poor_grades_count = 0
last_problem = ""
needs_break = False

while command != "Enough":
    task_name = command
    grade = int(input())
    grades_sum += grade
    task_count += 1
    last_problem = task_name
    if grade <= 4:
        poor_grades_count += 1
    if poor_grades_count == poor_grades_allowed:
        needs_break = True
        break
    command = input()
if needs_break:
    print(f"You need a break, {poor_grades_count} poor grades.")
else:
    average_score = grades_sum / task_count
    print(f"Average score: {average_score:.2f}")
    print(f"Number of problems: {task_count}")
    print(f"Last problem: {last_problem}")