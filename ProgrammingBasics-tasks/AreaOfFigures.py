figure = input()

if figure == "square":
    side = float(input())
    area = side * side
    print(f"{area:.3f}")
elif figure == "rectangle":
    side1 = float(input())
    side2 = float(input())
    area = side1 * side2
    print(f"{area:.3f}")
elif figure == "circle":
    radius = float(input())
    from math import pi
    area = pi * radius * radius
    print(f"{area:.3f}")
else:
    base = float(input())
    height = float(input())
    area = (base * height) / 2
    print(f"{area:.3f}")