year_type = input()
p = int(input())
h = int(input())

import math
saturday_sofia_games = ((48 - h) * 3) / 4
sunday_hometown_games = h

holiday_games = (p * 2) / 3

total_games = saturday_sofia_games + sunday_hometown_games + holiday_games


if year_type == "leap":
    leap_year_games = total_games * 0.15
    total_games += leap_year_games
total_games = math.floor(total_games)

print(total_games)