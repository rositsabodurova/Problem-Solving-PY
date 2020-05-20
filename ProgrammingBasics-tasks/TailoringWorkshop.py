tables_count = int(input())
tables_length = float(input())
tables_width = float(input())

cover_big = (tables_length + 0.60) * (tables_width + 0.60)
cover_small = (tables_length / 2) * (tables_length / 2)

money_total_usd = (cover_big * tables_count) * 7 + (cover_small * tables_count) * 9
money_total_bgn = money_total_usd * 1.85

print(f"{money_total_usd:.2f} USD")
print(f"{money_total_bgn:.2f} BGN")
