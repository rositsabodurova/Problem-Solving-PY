command = input()
goal_reached = False
total_steps = 0

while command != "Going home":
    steps = int(command)
    total_steps += steps
    if total_steps >= 10000:
        goal_reached = True
        break
    command = input()

if command == "Going home":
    final_steps = int(input())
    total_steps += final_steps
    if total_steps >= 10000:
        goal_reached = True

if goal_reached:
    print("Goal reached! Good job!")
else:
    difference = 10000 - total_steps
    print(f"{difference} more steps to reach goal.")