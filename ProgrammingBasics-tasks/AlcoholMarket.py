whiskey_price = float(input())
beer_quantity = float(input())
wine_quantity = float(input())
rakia_quantity = float(input())
whiskey_quantity = float(input())

rakia_price = whiskey_price * 0.5
wine_price = rakia_price * 0.6
beer_price = rakia_price * 0.2

whiskey_money = whiskey_price * whiskey_quantity
rakia_money = rakia_price * rakia_quantity
wine_money = wine_price * wine_quantity
beer_money = beer_price * beer_quantity

total_money = whiskey_money + rakia_money + wine_money + beer_money

print(f"{total_money:.2f}")