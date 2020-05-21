hours = int(input())
minutes = int(input())

total_minutes = (hours * 60) + minutes
new_time = total_minutes + 15

new_hours = new_time // 60
new_minutes = new_time % 60

if(new_hours >= 24):
    new_hours -= 24

if minutes < 10:
    print()