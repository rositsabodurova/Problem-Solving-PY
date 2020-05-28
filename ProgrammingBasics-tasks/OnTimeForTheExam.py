exam_hour = int(input())
exam_minutes = int(input())
arrival_hour = int(input())
arrival_minutes = int(input())

exam_time = (exam_hour * 60) + exam_minutes
arrival_time = (arrival_hour * 60) + arrival_minutes
difference = abs(exam_time - arrival_time)

if exam_time == arrival_time:
    print("On time")
elif arrival_time >= exam_time - 30 and arrival_time < exam_time:
    print("On time")
    print(f"{difference} minutes before the start")
elif arrival_time < exam_time - 30:
    print("Early")
    if difference <= 59:
        print(f"{difference} minutes before the start")
    else:
        diff_hours = difference // 60
        diff_minutes = difference % 60
        if diff_minutes <= 9:
            print(f"{diff_hours}:0{diff_minutes} hours before the start")
        else:
            print(f"{diff_hours}:{diff_minutes} hours before the start")
elif arrival_time > exam_time:
    print("Late")
    if difference <= 59:
        print(f"{difference} minutes after the start")
    else:
        diff_hours = difference // 60
        diff_minutes = difference % 60
        if diff_minutes <= 9:
            print(f"{diff_hours}:0{diff_minutes} hours after the start")
        else:
            print(f"{diff_hours}:{diff_minutes} hours after the start")