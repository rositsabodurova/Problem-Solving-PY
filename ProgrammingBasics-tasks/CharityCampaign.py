day_count = int(input())
bakers_count = int(input())
cakes_count = int(input())
waffles_count = int(input())
pancakes_count = int(input())

cake_money_per_day_baker = cakes_count * 45
waffle_money_per_day_baker = waffles_count * 5.80
pancakes_money_per_day_baker = pancakes_count * 3.20

money_per_day_baker = cake_money_per_day_baker + waffle_money_per_day_baker +pancakes_money_per_day_baker
money_per_day = money_per_day_baker * bakers_count

total_money = money_per_day * day_count
products_money = total_money / 8
final_money = total_money - products_money
print (f"{final_money:.2f}")