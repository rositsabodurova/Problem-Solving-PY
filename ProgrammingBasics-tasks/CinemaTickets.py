command = input()
standard_count = 0
student_count = 0
kid_count = 0
total_count = 0

while command != "Finish":
    capacity = int(input())
    ticket_type = input()
    current_tickets_count = 0
    while ticket_type != "End":

        total_count += 1
        current_tickets_count += 1
        if ticket_type == "standard":
            standard_count += 1
        elif ticket_type == "student":
            student_count += 1
        elif ticket_type == "kid":
            kid_count += 1
        if current_tickets_count == capacity:
            break
        ticket_type = input()
    current_movie_percentage = (current_tickets_count / capacity) * 100
    print(f"{command} - {current_movie_percentage:.2f}% full.")

    command = input()

student_percentage = (student_count / total_count) * 100
standard_percentage = (standard_count / total_count) * 100
kids_percentage = (kid_count / total_count) * 100

print(f"Total tickets: {total_count}")
print(f"{student_percentage:.2f}% student tickets.")
print(f"{standard_percentage:.2f}% standard tickets.")
print(f"{kids_percentage:.2f}% kids tickets.")