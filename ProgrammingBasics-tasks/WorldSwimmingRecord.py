current_record_seconds = float(input())
distance = float(input())
time_per_meter_seconds = float(input())

import math
delay = math.floor(distance / 15) * 12.5

total_time = distance * time_per_meter_seconds + delay
difference = abs(total_time - current_record_seconds)

if total_time < current_record_seconds:
    print(f"Yes, he succeeded! The new world record is {total_time:.2f} seconds.")
else:
    print(f"No, he failed! He was {difference:.2f} seconds slower.")