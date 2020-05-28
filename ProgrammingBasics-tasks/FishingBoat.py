budget = int(input())
season = input()
fishermen_count = int(input())

boat_price = 0

if season == "Spring":
   boat_price = 3000
elif season == "Winter":
    boat_price = 2600
else:
    boat_price = 4200

if fishermen_count <= 6:
    boat_price = boat_price * 0.9
elif fishermen_count <= 11:
    boat_price = boat_price * 0.85
else:
    boat_price = boat_price * 0.75

if fishermen_count % 2 == 0 and season != "Autumn":
    boat_price = boat_price * 0.95

difference = abs(boat_price - budget)

if boat_price > budget:
    print(f"Not enough money! You need {difference:.2f} leva.")
else:
    print(f"Yes! You have {difference:.2f} leva left.")