age = int(input())
laundry_machine_price = float(input())
toy_price = int(input())

total_sum = 0
toy_count = 0
gift = 0

for i in range(1, age + 1):

    if i % 2 == 0:
        gift += 10
        total_sum += gift - 1
    else:
        toy_count += 1

total_sum = total_sum + toy_price * toy_count
difference = abs(total_sum - laundry_machine_price)

if total_sum >= laundry_machine_price:
    print(f"Yes! {difference:.2f}")
else:
    print(f"No! {difference:.2f}")

