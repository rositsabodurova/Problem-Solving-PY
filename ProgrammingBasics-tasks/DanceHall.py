import math
hall_length = float(input()) * 100
hall_width = float(input()) * 100
wardrobe_side = float(input()) * 100

hall_area = hall_length * hall_width
wardrobe_area = wardrobe_side * wardrobe_side
bench = hall_area / 10
hall_area_free = hall_area - wardrobe_area - bench

dancers_count = math.floor(hall_area_free / 7040)
print(dancers_count)