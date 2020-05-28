month = input()
nights = int(input())

studio_price = 0
apartment_price = 0

if month in ("May", "October"):
    studio_price = nights * 50
    apartment_price = nights * 65
    if 7 < nights < 14:
        studio_price = studio_price * 0.95
    elif nights >= 14:
        studio_price = studio_price * 0.7
        apartment_price = apartment_price * 0.9
    print(f"Apartment: {apartment_price:.2f} lv.")
    print(f"Studio: {studio_price:.2f} lv.")
elif month in ("June", "September"):
    studio_price = nights * 75.2
    apartment_price = nights * 68.7
    if nights > 14:
        studio_price *= 0.8
        apartment_price *= 0.9
    print(f"Apartment: {apartment_price:.2f} lv.")
    print(f"Studio: {studio_price:.2f} lv.")
else:
    studio_price = nights * 76
    apartment_price = nights * 77
    if nights > 14:
        apartment_price *= 0.9
    print(f"Apartment: {apartment_price:.2f} lv.")
    print(f"Studio: {studio_price:.2f} lv.")
