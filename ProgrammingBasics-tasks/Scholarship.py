income = float(input())
average_grades = float(input())
minimal_wage = float(input())

is_eligible_social = False
is_eligible_excellent = False
scholarship_amount_social = 0
scholarship_amount_excellent = 0

import math

if income < minimal_wage and average_grades >= 4.5:
    is_eligible_social = True
    scholarship_amount_social = math.floor(minimal_wage * 0.35)

if average_grades >= 5.5:
    is_eligible_excellent = True
    scholarship_amount_excellent = math.floor(average_grades * 25)

if is_eligible_excellent & is_eligible_social:
    if scholarship_amount_excellent >= scholarship_amount_social:
        print(f"You get a scholarship for excellent results {scholarship_amount_excellent} BGN")
    else:
        print(f"You get a Social scholarship {scholarship_amount_social} BGN")
elif is_eligible_social and is_eligible_excellent == False:
    print(f"You get a Social scholarship {scholarship_amount_social} BGN")
elif is_eligible_excellent and is_eligible_social == False:
    print(f"You get a scholarship for excellent results {scholarship_amount_excellent} BGN")
else:
    print("You cannot get a scholarship!")
